# Copyright 2011 Denali Systems, Inc.
# All Rights Reserved.
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
Cdrom interface (1.1 extension).
"""
from novaclient import base


class Cdrom(base.Resource):
    """
    DEPRECATED: A Cdrom is an extra block level storage to the OpenStack
    instances.
    """
    NAME_ATTR = 'display_name'

    def __repr__(self):
        return "<Cdrom: %s>" % self.host


class CdromManager(base.ManagerWithFind):
    """
    DEPRECATED: Manage :class:`Cdrom` resources.
    """
    resource_class = Cdrom

    def list(self, server):
        """
        DEPRECATED: Get a list of all cdroms.

        :rtype: list of :class:`Cdrom`
        """
        return self._list("/os-phy_cdrom?instance_id=%s" % server,
                          "host_cdrom_list")

    def create_server_cdrom(self, server_id, cdrom_name):
        """
        Attach a cdrom identified by the cdrom NAME to the given server ID

        :param server_id: The ID of the server
        :param cdrom_name: The NAME of the cdrom to attach.
        :rtype: :class:`cdrom`
        """
        body = {
            'attached_cdrom': {
                'instance_id': server_id,
                'cdrom': cdrom_name
            }
        }
        resp, body = self.api.client.post("/os-phy_cdrom/attach_cdrom",
                                          body=body)
        return self.convert_into_with_meta(body, resp)

    def delete_server_cdrom(self, server_id, cdrom_name):
        body = {
            'detached_cdrom': {
                'instance_id': server_id,
                'cdrom': cdrom_name
            }
        }
        resp, body = self.api.client.post("/os-phy_cdrom/detach_cdrom",
                                          body=body)
        return self.convert_into_with_meta(body, resp)
