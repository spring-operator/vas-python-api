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
from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
from vas.rabbitmq.RabbitMqLogs import RabbitMqLogs
from vas.rabbitmq.RabbitMqNode import RabbitMqNode
from vas.rabbitmq.RabbitMqNodeInstance import RabbitMqNodeInstance
from vas.test.StubClient import StubClient

class TestRabbitMqNodeInstance(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instance = RabbitMqNodeInstance(self.__client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/')

    def test_attributes(self):
        self.assertIsInstance(self.__instance.group_instance, RabbitMqGroupInstance)
        self.assertIsInstance(self.__instance.logs, RabbitMqLogs)
        self.assertEqual('example', self.__instance.name)
        self.assertIsInstance(self.__instance.node, RabbitMqNode)
        self.assertEqual('STOPPED', self.__instance.state)
        self.assertIsInstance(self.__instance.security, Security)

    def test_start(self):
        self.__instance.start()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/state/', {'status': 'STARTED'})

    def test_stop(self):
        self.__instance.stop()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/state/', {'status': 'STOPPED'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instance)),
            '__repr__ method has not been specified')
        eval(repr(self.__instance))
