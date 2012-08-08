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
from vas.tc_server.TcServerGroup import TcServerGroup
from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerInstallation import TcServerInstallation
from vas.tc_server.TcServerInstallationImage import TcServerInstallationImage
from vas.tc_server.TcServerTemplates import TcServerTemplates
from vas.test.StubClient import StubClient

class TestTcServerInstallation(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__installation = TcServerInstallation(self.__client,
            'https://localhost:8443/tc-server/v1/groups/1/installations/2/')

    def test_attributes(self):
        self.assertEqual(['7.0.27.A.RELEASE'], self.__installation.runtime_versions)
        self.assertEqual('2.7.0.RELEASE', self.__installation.version)
        self.assertIsInstance(self.__installation.group, TcServerGroup)
        self.assertEqual(
            [TcServerGroupInstance(self.__client, 'https://localhost:8443/tc-server/v1/groups/1/instances/3/'),
             TcServerGroupInstance(self.__client, 'https://localhost:8443/tc-server/v1/groups/1/instances/4/'), ],
            self.__installation.instances)
        self.assertIsInstance(self.__installation.installation_image, TcServerInstallationImage)
        self.assertIsInstance(self.__installation.security, Security)
        self.assertIsInstance(self.__installation.templates, TcServerTemplates)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__installation)),
            '__repr__ method has not been specified')
        eval(repr(self.__installation))
