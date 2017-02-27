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
Iso interface (1.1 extension).
"""

from novaclient import base


class Iso(base.Resource):
    """
    DEPRECATED: A Iso is an extra block level storage to the OpenStack
    instances.
    """
    NAME_ATTR = 'display_name'

    def __repr__(self):
        return "<Iso: %s>" % self.id


class IsoManager(base.ManagerWithFind):
    """
    DEPRECATED: Manage :class:`Iso` resources.
    """
    resource_class = Iso

    def list(self, server):
        """
        DEPRECATED: Get a list of all isos.

        :rtype: list of :class:`Iso`
        """
        pass

    def attach_iso(self, server, iso):
        """
        Attach a iso identified by the iso id to the given server ID

        :param server: The ID of the server
        :param iso: The ID of the iso to attach.
        :rtype: :class:`Iso`
        """
        path = '/servers/%s/action' % server
        post_body = {"ChangeISO": {"iso": iso}}
        resp, body = self.api.client.post(path, body=post_body)
        return self.convert_into_with_meta(body, resp)

    def detach_iso(self, server):
        """
        Detach a iso identified by the iso id to the given server ID

        :param server: The ID of the server
        :param iso: The ID of the iso to attach.
        :rtype: :class:`Iso`
        """
        path = '/servers/%s/action' % server
        post_body = {"ChangeISO": {"iso": None}}
        resp, body = self.api.client.post(path, body=post_body)
        return self.convert_into_with_meta(body, resp)
