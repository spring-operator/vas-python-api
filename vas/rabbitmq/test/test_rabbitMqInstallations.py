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
from vas.shared.InstallationImage import InstallationImage
from vas.shared.Security import Security
from vas.rabbitmq.RabbitMqInstallation import RabbitMqInstallation
from vas.rabbitmq.RabbitMqInstallations import RabbitMqInstallations
from vas.test.StubClient import StubClient

class TestRabbitMqInstallations(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__installations = RabbitMqInstallations(self.__client,
            'https://localhost:8443/rabbitmq/v1/groups/1/installations/')

    def test_delete(self):
        self.__installations.delete(
            RabbitMqInstallation(self.__client, 'https://localhost:8443/rabbitmq/v1/groups/1/installations/2/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/1/installations/2/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/rabbitmq/v1/groups/1/installations/2/'

        group = self.__installations.create(
            InstallationImage(self.__client, 'https://localhost:8443/rabbitmq/v1/installation-images/0/'))

        self.assertIsInstance(group, RabbitMqInstallation)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/0/installations/',
                {'image': 'https://localhost:8443/rabbitmq/v1/installation-images/0/'}, 'installation')

    def test_attributes(self):
        self.assertIsInstance(self.__installations.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__installations._create_item(self.__client,
                'https://localhost:8443/rabbitmq/v1/groups/1/installations/2/'), RabbitMqInstallation)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__installations:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__installations)),
            '__repr__ method has not been specified')
        eval(repr(self.__installations))