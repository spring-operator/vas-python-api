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


from vas.test.VasTestCase import VasTestCase
from vas.web_server.Groups import Groups
from vas.web_server.InstallationImages import InstallationImages
from vas.web_server.Nodes import Nodes
from vas.web_server.WebServer import WebServer

class TestWebServer(VasTestCase):
    def test_webserver(self):
        self._assert_item(WebServer(self._client, 'https://localhost:8443/web-server/v1/'), [
            ('groups', lambda actual: self.assertIsInstance(actual, Groups)),
            ('installation_images', lambda actual: self.assertIsInstance(actual, InstallationImages)),
            ('nodes', lambda actual: self.assertIsInstance(actual, Nodes))
        ], False)
