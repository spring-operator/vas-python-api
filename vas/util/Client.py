# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import json
import requests
import time
from vas.util.LinkUtils import LinkUtils
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class Client:

    __CHUNK_SIZE = 8192

    __CONTENT_TYPE_JSON = 'application/json'

    __CONTENT_TYPE_MULTIPART = 'multipart/mixed'

    __HEADER_CONTENT_TYPE = 'Content-Type'

    __HEADER_LOCATION = 'Location'

    __TASK_POLLING_INTERVAL = 1

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get(self, location):
        response = self.__do_request('GET', location)

        status_code = response.status_code
        if status_code == requests.codes.OK:
            content_type = response.headers[self.__HEADER_CONTENT_TYPE]
            if content_type == self.__CONTENT_TYPE_JSON:
                return response.json
            elif content_type is None:
                # TODO Remove this once VMS-1121 has been fixed
                return response.iter_content(self.__CHUNK_SIZE)
            else:
                raise VFabricAdministrationServerError('Unknown payload type: ' + content_type)
        else:
            raise VFabricAdministrationServerError('Unexpected status code: ' + status_code)

    def delete(self, location):
        response = self.__do_request('DELETE', location)
        if response.status_code == requests.codes.OK:
            return
        elif response.status_code == requests.codes.ACCEPTED:
            self.__await_task(response.headers[self.__HEADER_LOCATION])
        else:
            self.__raise_exception(response)

    def post(self, location, payload, rel=None):
        if isinstance(payload, dict) or isinstance(payload, list):
            headers = {self.__HEADER_CONTENT_TYPE: self.__CONTENT_TYPE_JSON}
            encoded_body = json.dumps(payload)
        else:
            raise VFabricAdministrationServerError('Unknown payload type')

        response = self.__do_request('POST', location, headers=headers, body=encoded_body)
        if response.status_code == requests.codes.ACCEPTED:
            return self.__await_task(response.headers[self.__HEADER_LOCATION], rel)
        else:
            self.__raise_exception(response)

    def post_image(self, location, metadata, file):
        with open(file, 'rb') as data:
            encoded_body = {'metadata': ('metadata.json', json.dumps(metadata))}
            encoded_files = {'data': data}

            response = self.__do_request('POST', location, body=encoded_body, files=encoded_files)
            if response.status_code == requests.codes.CREATED:
                return response.headers[self.__HEADER_LOCATION]
            else:
                self.__raise_exception(response)

    def __do_request(self, method, location, headers=None, body=None, files=None):
        return requests.request(method, location, headers=headers, data=body, files=files,
                                auth=(self.__username, self.__password), verify=False)

    def __await_task(self, task_location, rel=None):
        while True:
            task = self.get(task_location)
            status = task['status']

            if 'PENDING' == status or 'IN_PROGRESS' == status:
                time.sleep(self.__TASK_POLLING_INTERVAL)
            elif 'SUCCESS' == status:
                self.delete(task_location)

                if rel is not None:
                    return LinkUtils.get_link(task, rel)
                else:
                    return
            else:
                raise VFabricAdministrationServerError(task['message'], task['detail'])


    def __raise_exception(self, response):
        reasons = []

        for reason in response.json['reasons']:
            reasons.append(reason['message'])

        raise VFabricAdministrationServerError(*reasons)