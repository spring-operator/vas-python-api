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


from datetime import datetime
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.tc_server.TcServerLog import TcServerLog
from vas.tc_server.TcServerNodeInstance import TcServerNodeInstance
from vas.test.StubClient import StubClient

class TestTcServerLog(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__log = TcServerLog(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/')

    def test_attributes(self):
        self.assertEqual(datetime(2012, 5, 24, 15, 20, 56), self.__log.last_modified)
        self.assertEqual('catalina.out', self.__log.name)
        self.assertEqual(17638, self.__log.size)
        self.assertIsInstance(self.__log.node_instance, TcServerNodeInstance)
        self.assertIsInstance(self.__log.security, Security)

    def test_content(self):
        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-instances-logs-content\n', self.__log.content())
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/content/')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-instances-logs-content\n', self.__log.content(start_line='1'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/content/?start-line=1')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-instances-logs-content\n', self.__log.content(end_line='2'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/content/?end-line=2')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-instances-logs-content\n', self.__log.content(start_line='1', end_line='2'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/logs/4/content/?start-line=1&end-line=2')
