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


import re
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.gemfire.GemFireAgentNodeInstance import GemFireAgentNodeInstance
from vas.gemfire.GemFireAgentNodeInstances import GemFireAgentNodeInstances
from vas.test.StubClient import StubClient

class TestGemFireAgentNodeInstances(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instances = GemFireAgentNodeInstances(self.__client,
            'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/')

    def test_attributes(self):
        self.assertIsInstance(self.__instances.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__instances._create_item(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/'),
            GemFireAgentNodeInstance)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__instances:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instances)),
            '__repr__ method has not been specified')
        eval(repr(self.__instances))
