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


from vas.shared.LiveConfiguration import LiveConfiguration

class GemFireCacheServerLiveConfiguration(LiveConfiguration):
    """A GemFire cache server live configuration

    :ivar `vas.gemfire.GemFireCacheServerGroupInstance` instance: The configuration's parent group instance
    :ivar str path: The path of the configuration
    :ivar int size: The size of the configuration
    :ivar str content:  The contents of the configuration
    :ivar `vas.shared.Security` security:   The security configuration for the type
    """

    __REL_GROUP_INSTANCE = 'cache-server-group-instance'

    def __init__(self, client, location):
        super(GemFireCacheServerLiveConfiguration, self).__init__(client, location, self.__REL_GROUP_INSTANCE)

    def _create_group_instance(self, client, location):
        return GemFireCacheServerGroupInstance(client, location)

from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance