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
from vas.test.StubClient import StubClient
from vas.tc_server.TcServerNode import TcServerNode
from vas.tc_server.TcServerNodes import TcServerNodes

class TestTcServerNodes(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__nodes = TcServerNodes(self.__client, 'https://localhost:8443/tc-server/v1/nodes/')

    def test_attributes(self):
        self.assertIsInstance(self.__nodes.security, Security)

    def test__create_item(self):
        self.assertIsInstance(self.__nodes._create_item(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/'),
            TcServerNode)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__nodes:
            count += 1

        self.assertEqual(2, count)