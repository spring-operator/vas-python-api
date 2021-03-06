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


from vas.web_server.Instances import Instance
from vas.web_server.Logs import Logs
from vas.web_server.NodeInstances import NodeInstances, NodeInstance
from vas.web_server.NodeLiveConfigurations import NodeLiveConfigurations
from vas.web_server.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestNodeInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(NodeInstances(self._client, 'https://localhost:8443/web-server/v1/nodes/0/instances/'))

    def test_detail(self):
        self._assert_item(NodeInstance(self._client, 'https://localhost:8443/web-server/v1/nodes/0/instances/3/'), [
            ('group_instance', lambda actual: self.assertIsInstance(actual, Instance)),
            ('live_configurations', lambda actual: self.assertIsInstance(actual, NodeLiveConfigurations)),
            ('logs', lambda actual: self.assertIsInstance(actual, Logs)),
            ('name', 'example'),
            ('node', lambda actual: self.assertIsInstance(actual, Node)),
            ('state', 'STOPPED')
        ])

    def test_start(self):
        NodeInstance(self._client, 'https://localhost:8443/web-server/v1/nodes/0/instances/3/').start()
        self._assert_post('https://localhost:8443/web-server/v1/nodes/0/instances/3/state/', {'status': 'STARTED'})

    def test_stop(self):
        NodeInstance(self._client, 'https://localhost:8443/web-server/v1/nodes/0/instances/3/').stop()
        self._assert_post('https://localhost:8443/web-server/v1/nodes/0/instances/3/state/', {'status': 'STOPPED'})
