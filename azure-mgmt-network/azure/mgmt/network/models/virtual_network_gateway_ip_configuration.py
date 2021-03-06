# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class VirtualNetworkGatewayIPConfiguration(SubResource):
    """
    IpConfiguration for Virtual network gateway

    :param id: Resource Id
    :type id: str
    :param private_ip_address: Gets or sets the privateIPAddress of the IP
     Configuration
    :type private_ip_address: str
    :param private_ip_allocation_method: Gets or sets PrivateIP allocation
     method (Static/Dynamic). Possible values include: 'Static', 'Dynamic'
    :type private_ip_allocation_method: str
    :param subnet: Gets or sets the reference of the subnet resource
    :type subnet: :class:`SubResource <azure.mgmt.network.models.SubResource>`
    :param public_ip_address: Gets or sets the reference of the PublicIP
     resource
    :type public_ip_address: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'IPAllocationMethod'},
        'subnet': {'key': 'properties.subnet', 'type': 'SubResource'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, private_ip_address=None, private_ip_allocation_method=None, subnet=None, public_ip_address=None, provisioning_state=None, name=None, etag=None, **kwargs):
        super(VirtualNetworkGatewayIPConfiguration, self).__init__(id=id, **kwargs)
        self.private_ip_address = private_ip_address
        self.private_ip_allocation_method = private_ip_allocation_method
        self.subnet = subnet
        self.public_ip_address = public_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
