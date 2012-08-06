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


from vas.shared.MutableCollectionType import MutableCollectionType

class Groups(MutableCollectionType):
    """A collection of abstract groups

    :ivar `vas.shared.Security` security:   The security configuration for the collection of abstract groups
    """

    __COLLECTION_KEY = 'groups'

    __REL_GROUP = 'group'

    def __init__(self, client, location):
        super(Groups, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, name, nodes):
        """Create a new group

        :type name:     :obj:`str`
        :param name:    The name of the group
        :type nodes:    :obj:`list` of :class:`vas.shared.Node`
        :param nodes:   The collection of nodes to be included in the group
        :rtype:         :class:`vas.shared.GroupInstances`
        :return:        The newly created group
        """

        location = self._client.post(self._location_self,
                {'name': name, 'nodes': [node._location_self for node in nodes]}, self.__REL_GROUP)
        return self._create_item(self._client, location)