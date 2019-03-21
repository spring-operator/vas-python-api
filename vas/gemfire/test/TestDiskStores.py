# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from datetime import datetime
from vas.gemfire.CacheServerNodeInstances import CacheServerNodeInstance
from vas.gemfire.DiskStores import DiskStores, DiskStore
from vas.test.VasTestCase import VasTestCase

class TestDiskStores(VasTestCase):
    def test_list(self):
        self._assert_collection(
            DiskStores(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/disk-stores/'))

    def test_detail(self):
        self._assert_item(DiskStore(self._client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/disk-stores/4/'), [
            ('last_modified', datetime(2012, 5, 24, 15, 20, 56)),
            ('name', 'example.gfs'),
            ('size', 17638),
            ('content', 'nodes-cache-server-instances-disk-stores-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, CacheServerNodeInstance))
        ])

    def test_delete(self):
        self._assert_deletable(DiskStore(self._client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/disk-stores/4/'))
