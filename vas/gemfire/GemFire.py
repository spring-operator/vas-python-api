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


from vas.shared.ComponentType import ComponentType

class GemFire(ComponentType):
    """The GemFire component of the vFabric Administration Server

    :ivar `vas.gemfire.GemFireGroups` groups:    The collection of groups
    :ivar `vas.gemfire.GemFireInstallationImages` installation_images:  The collection of installation images
    :ivar `vas.gemfire.GemFireNodes` nodes: The collection of nodes
    :ivar `vas.gemfire.GemFireApplicationCodeImages` application_code_images: The collection of application code images
    """

    __REL_APPLICATION_CODE_IMAGES = 'application-code-images'

    __ROOT_PATH = '/gemfire/v1/'

    def __init__(self, client, location_stem):
        super(GemFire, self).__init__(client, location_stem.format(self.__ROOT_PATH))

        self.application_code_images = GemFireApplicationCodeImages(client, self._links[self.__REL_APPLICATION_CODE_IMAGES][0])
        self.__location_stem = location_stem

    def _create_groups(self, client, location):
        return GemFireGroups(client, location)

    def _create_installation_images(self, client, location):
        return GemFireInstallationImages(client, location)

    def _create_nodes(self, client, location):
        return GemFireNodes(client, location)

    def __repr__(self):
        return "{}(client={}, location_stem={})".format(self.__class__.__name__, self._client,
            repr(self.__location_stem))

from vas.gemfire.GemFireApplicationCodeImages import GemFireApplicationCodeImages
from vas.gemfire.GemFireGroups import GemFireGroups
from vas.gemfire.GemFireInstallationImages import GemFireInstallationImages
from vas.gemfire.GemFireNodes import GemFireNodes