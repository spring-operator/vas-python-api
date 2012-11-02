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


from vas.shared.Logs import Logs, Log

class AgentLogs(Logs):
    """Used to enumerate an agent node instance's logs

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(AgentLogs, self).__init__(client, location, AgentLog)


class AgentLog(Log):
    """A log file in an agent node instance

    :ivar `vas.sqlfire.AgentNodeInstances.AgentNodeInstance`    instance:       The node instance that the log belongs
                                                                                to
    :ivar `datetime.datetime`                                   last_modified:  The last modified stamp of the log
    :ivar str                                                   name:           The name of the log
    :ivar `vas.shared.Security.Security`                        security:       The resource's security
    :ivar int                                                   size:           The size of the log
    """

    def __init__(self, client, location):
        super(AgentLog, self).__init__(client, location, 'agent-node-instance', AgentNodeInstance)


from vas.sqlfire.AgentNodeInstances import AgentNodeInstance
