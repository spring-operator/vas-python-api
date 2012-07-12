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


from unittest.case import TestCase
from vas.shared.Security import Security
from vas.tc_server.TcServerRevisionImage import TcServerRevisionImage
from vas.tc_server.TcServerRevisionImages import TcServerRevisionImages
from vas.test.StubClient import StubClient

class TestTcServerRevisionImages(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__revision_images = TcServerRevisionImages(self.__client,
            'https://localhost:8443/tc-server/v1/revision-images/')

    def test_delete(self):
        self.__revision_images.delete(
            TcServerRevisionImage(self.__client, 'https://localhost:8443/tc-server/v1/revision-images/0/'))
        self.__client.delegate.delete.assert_called_once_with('https://localhost:8443/tc-server/v1/revision-images/0/')

    def test_create(self):
        self.__client.delegate.post_multipart.return_value = 'https://localhost:8443/tc-server/v1/revision-images/0/'

        revision_image = self.__revision_images.create('example', '1.0.0', '/tmp/petcare-1.0.0.RELEASE.war')

        self.assertIsInstance(revision_image, TcServerRevisionImage)
        self.__client.delegate.post_multipart.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/revision-images/',
                {'name': 'example', 'version': '1.0.0'}, '/tmp/petcare-1.0.0.RELEASE.war')

    def test_attributes(self):
        self.assertIsInstance(self.__revision_images.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__revision_images._create_item(self.__client, 'https://localhost:8443/tc-server/v1/revision-images/0/')
            , TcServerRevisionImage)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__revision_images:
            count += 1

        self.assertEqual(2, count)
