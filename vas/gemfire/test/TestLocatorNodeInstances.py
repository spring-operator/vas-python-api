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


from vas.gemfire.LocatorInstances import LocatorInstance
from vas.gemfire.LocatorLogs import LocatorLogs
from vas.gemfire.LocatorNodeInstances import LocatorNodeInstances, LocatorNodeInstance
from vas.gemfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfigurations
from vas.gemfire.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestLocatorNodeInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            LocatorNodeInstances(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/locator-instances/'))

    def test_detail(self):
        self._assert_item(
            LocatorNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/locator-instances/3/'), [
                ('address', '192.168.0.2'),
                ('group_instance', lambda actual: self.assertIsInstance(actual, LocatorInstance)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, LocatorNodeLiveConfigurations)),
                ('logs', lambda actual: self.assertIsInstance(actual, LocatorLogs)),
                ('name', 'example'),
                ('node', lambda actual: self.assertIsInstance(actual, Node)),
                ('peer', lambda actual: self.assertTrue(actual)),
                ('port', 41111),
                ('state', 'STOPPED'),
                ('server', lambda actual: self.assertTrue(actual))
            ])

    def test_start(self):
        LocatorNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/locator-instances/3/').start()
        self._assert_post('https://localhost:8443/gemfire/v1/nodes/0/locator-instances/3/state/', {'status': 'STARTED'})

    def test_stop(self):
        LocatorNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/locator-instances/3/').stop()
        self._assert_post('https://localhost:8443/gemfire/v1/nodes/0/locator-instances/3/state/', {'status': 'STOPPED'})
