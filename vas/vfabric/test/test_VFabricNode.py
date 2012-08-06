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
from vas.vfabric.VFabricNode import VFabricNode

class TestVFabricNode(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__node = VFabricNode(self.__client, 'https://localhost:8443/vfabric/v1/nodes/0/')

    def test_attributes(self):
        self.assertEqual('/opt/vmware/vfabric-administration-agent', self.__node.agent_home)
        self.assertEqual('x64', self.__node.architecture)
        self.assertEqual(['example-host'], self.__node.host_names)
        self.assertEqual(['192.168.0.2', '127.0.0.1'], self.__node.ip_addresses)
        self.assertEqual({'a': 'alpha', 'b': 'bravo'}, self.__node.metadata)
        self.assertEqual('Linux', self.__node.operating_system)
        self.assertIsInstance(self.__node.security, Security)