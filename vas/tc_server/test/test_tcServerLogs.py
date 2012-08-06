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
from vas.tc_server.TcServerLog import TcServerLog
from vas.tc_server.TcServerLogs import TcServerLogs
from vas.test.StubClient import StubClient

class TestTcServerLogs(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__logs = TcServerLogs(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/')

    def test_delete(self):
        self.__logs.delete(
            TcServerLog(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/')

    def test_attributes(self):
        self.assertIsInstance(self.__logs.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__logs._create_item(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/'),
            TcServerLog)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__logs:
            count += 1

        self.assertEqual(2, count)