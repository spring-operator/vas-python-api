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


from vas.shared.Configuration import Configuration

class LiveConfiguration(Configuration):
    """A live configuration file in an instance

    :ivar str                               content:                The configuration's content
    :ivar `vas.shared.Instance.Instance`    instance:               The instance that owns the configuration
    :ivar str                               path:                   The configuration's path
    :ivar list                              node_configurations:    The configuration's node configurations
    :ivar `vas.shared.Security.Security`    security:               The resource's security
    :ivar int                               size:                   The configuration's size
    """

    @property
    def node_configurations(self):
        self.__node_live_configurations = self.__node_live_configurations or self._create_resources_from_links(
            'node-live-configuration', self.__node_live_configuration_class)
        return self.__node_live_configurations

    def __init__(self, client, location, instance_type, instance_class, node_live_configuration_class):
        super(LiveConfiguration, self).__init__(client, location, instance_type, instance_class)
        self.__node_live_configuration_class = node_live_configuration_class

    def reload(self):
        """Reloads the live configuration's details from the server"""

        super(LiveConfiguration, self).reload()
        self.__node_live_configurations = None
