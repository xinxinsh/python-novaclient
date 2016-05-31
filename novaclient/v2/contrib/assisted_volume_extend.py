# Copyright (C) 2016, Chinac, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Assisted volume extend - to be used by Cinder and not end users.
"""

from novaclient import base


class Volume(base.Resource):
    def __repr__(self):
        return "<Volume: %s>" % self.id

    def delete(self):
        """
        Delete this volume.

        :returns: An instance of novaclient.base.TupleWithMeta
        """
        return self.manager.delete(self)


class AssistedVolumeManager(base.Manager):
    resource_class = Volume

    def create(self, volume_id, extend_info):
        body = {'volume': {'volume_id': volume_id,
                           'extend_info': extend_info}}
        return self._create('/os-assisted-volume-extend', body, 'volume')

manager_class = AssistedVolumeManager
name = 'assisted_volume_extend'
