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


import vas.shared.InstallationImages

class InstallationImages(vas.shared.InstallationImages.InstallationImages):
    """Used to enumerate, create, and delete SqlFire installation images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(InstallationImages, self).__init__(client, location, InstallationImage)


class InstallationImage(vas.shared.InstallationImages.InstallationImage):
    """A SqlFire installation image

    :ivar `vas.sqlfire.Installations.Installations` installations:  The installations that have been created from the
                                                                    installation image
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar int                                       size:           The installation image's size
    :ivar str                                       version:        The installation image's version
    """

    def __init__(self, client, location):
        super(InstallationImage, self).__init__(client, location, Installation)


from vas.sqlfire.Installations import Installation
