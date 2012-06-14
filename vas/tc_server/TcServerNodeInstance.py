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


from vas.shared.NodeInstance import NodeInstance

class TcServerNodeInstance(NodeInstance):
    """A tc Server group instance

    :ivar `vas.tc_server.TcServerGroupInstance` group_instance: The group instance that the node instance is a member of
    :ivar str layout:   The layout of the group instance
    :ivar `vas.tc_server.TcServerLogs` logs: The collection of logs
    :ivar str name: The name of the group instance
    :ivar `vas.tc_server.TcServerNode` node: The node instance's parent node
    :ivar `vas.tc_server.TcServerNodeApplications` node_applications: The collection of node applications
    :ivar str runtime_version:  The runtime version of the group instance
    :ivar `vas.shared.Security` security: The security configuration for the node instance
    :ivar str services: The services configured in the group instance
    :ivar str state:    The current state of the node instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """
    __KEY_LAYOUT = 'layout'

    __KEY_NAME = 'name'

    __KEY_RUNTIME_VERSION = 'runtime-version'

    __KEY_SERVICES = 'services'

    __REL_GROUP_INSTANCE = 'group-instance'

    __REL_NODE_APPLICATIONS = 'node-applications'

    def __init__(self, client, location):
        super(TcServerNodeInstance, self).__init__(client, location)

        self.group_instance = TcServerGroupInstance(client, self._links[self.__REL_GROUP_INSTANCE][0])
        self.layout = self._details[self.__KEY_LAYOUT]
        self.name = self._details[self.__KEY_NAME]
        self.node_applications = TcServerNodeApplications(client, self._links[self.__REL_NODE_APPLICATIONS][0])
        self.runtime_version = self._details[self.__KEY_RUNTIME_VERSION]
        self.services = self._details[self.__KEY_SERVICES]

    def _create_logs(self, client, location):
        return TcServerLogs(client, location)

    def _create_node(self, client, location):
        return TcServerNode(client, location)

from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerLogs import TcServerLogs
from vas.tc_server.TcServerNode import TcServerNode
from vas.tc_server.TcServerNodeApplications import TcServerNodeApplications
