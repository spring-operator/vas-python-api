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


from vas.shared.Collection import Collection
from vas.shared.LiveConfiguration import LiveConfiguration

class AgentLiveConfigurations(Collection):
    """Used to enumerate a agent instance's live configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(AgentLiveConfigurations, self).__init__(client, location, 'live-configurations',
            AgentLiveConfiguration)


class AgentLiveConfiguration(LiveConfiguration):
    """A live configuration file in a agent instance

    :ivar str                                           content:                The configuration's content
    :ivar `vas.sqlfire.AgentInstances.AgentInstance`    instance:               The instance that owns the configuration
    :ivar str                                           path:                   The configuration's path
    :ivar list                                          node_configurations:    The configuration's node configurations
    :ivar `vas.shared.Security.Security`                security:               The resource's security
    :ivar int                                           size:                   The configuration's size
    """

    def __init__(self, client, location):
        super(AgentLiveConfiguration, self).__init__(client, location, 'agent-group-instance', AgentInstance,
            AgentNodeLiveConfiguration)


from vas.sqlfire.AgentInstances import AgentInstance
from vas.sqlfire.AgentNodeLiveConfigurations import AgentNodeLiveConfiguration
