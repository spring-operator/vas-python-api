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


from vas.sqlfire.Groups import Group
from vas.sqlfire.Installations import Installation
from vas.sqlfire.ServerInstances import ServerInstances, ServerInstance
from vas.sqlfire.ServerLiveConfigurations import ServerLiveConfigurations
from vas.sqlfire.ServerNodeInstances import ServerNodeInstance
from vas.sqlfire.ServerPendingConfigurations import ServerPendingConfigurations
from vas.test.VasTestCase import VasTestCase

class TestServerInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            ServerInstances(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/'))

    def test_create_no_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/0/server-instances/'
        self._return_location('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/')

        instance = ServerInstances(self._client, location).create(Installation(self._client, installation_location),
            'example')

        self.assertIsInstance(instance, ServerInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location}, 'server-group-instance')

    def test_create_all_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/0/server-instances/'
        self._return_location('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/')

        instance = ServerInstances(self._client, location).create(Installation(self._client, installation_location),
            'example', 'bind.address', 'client.bind.address', 1234, 90, '-Xmx512M', ['-Da=alpha'], '-Xmx1024M', True)

        self.assertIsInstance(instance, ServerInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location, 'bind-address': 'bind.address',
             'client-bind-address': 'client.bind.address', 'client-port': 1234, 'critical-heap-percentage': 90,
             'initial-heap': '-Xmx512M', 'jvm-options': ['-Da=alpha'], 'max-heap': '-Xmx1024M', 'run-netserver': True},
            'server-group-instance')

    def test_detail(self):
        self._assert_item(
            ServerInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/'), [
                ('bind_address', 'bind.address'),
                ('client_bind_address', 'client.bind.address'),
                ('client_port', 1234),
                ('critical_heap_percentage', 90),
                ('initial_heap', '512M'),
                ('jvm_options', ['-Da=alpha']),
                ('name', 'example'),
                ('state', 'STOPPED'),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, ServerLiveConfigurations)),
                ('max_heap', '1024M'),
                ('node_instances', [
                    ServerNodeInstance(self._client, 'https://localhost:8443/sqlfire/v1/nodes/1/server-instances/6/'),
                    ServerNodeInstance(self._client, 'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/5/')
                ]),
                ('pending_configurations', lambda actual: self.assertIsInstance(actual, ServerPendingConfigurations)),
                ('run_netserver', lambda actual: self.assertTrue(actual))
            ])


    def test_start_parallel(self):
        ServerInstance(self._client,
            'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/').start()
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        ServerInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/').start(
            True)
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        ServerInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/').stop()
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        ServerInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/').stop(
            True)
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update_no_optionals(self):
        location = 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/'

        ServerInstance(self._client, location).update()

        self._assert_post(location, {})

    def test_update_all_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/'

        ServerInstance(self._client, location).update(Installation(self._client, installation_location), 'bind.address',
            'client.bind.address', 1234, 90, '-Xmx512M', ['-Da=alpha'], '-Xmx1024M', True)

        self._assert_post(location, {'installation': installation_location, 'bind-address': 'bind.address',
                                     'client-bind-address': 'client.bind.address', 'client-port': 1234,
                                     'critical-heap-percentage': 90,
                                     'initial-heap': '-Xmx512M', 'jvm-options': ['-Da=alpha'], 'max-heap': '-Xmx1024M',
                                     'run-netserver': True})

    def test_delete(self):
        self._assert_deletable(
            ServerInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/server-instances/4/'))
