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


import vas.shared.PendingConfigurations

class PendingConfigurations(vas.shared.PendingConfigurations.PendingConfigurations):
    """Used to enumerate an instance's pending configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(PendingConfigurations, self).__init__(client, location, PendingConfiguration)


class PendingConfiguration(vas.shared.PendingConfigurations.PendingConfiguration):
    """A configuration file that is pending

    :ivar str                                   content:    The configuration's content
    :ivar `vas.tc_server.Instances.Instance`    instance:   The instance that owns the configuration
    :ivar str                                   path:       The configuration's path
    :ivar `vas.shared.Security.Security`        security:   The resource's security
    :ivar int                                   size:       The configuration's size
    """

    def __init__(self, client, location):
        super(PendingConfiguration, self).__init__(client, location, 'group-instance', Instance)


from vas.tc_server.Instances import Instance
