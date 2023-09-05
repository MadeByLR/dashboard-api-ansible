#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_switch_stacks_routing_interfaces_dhcp_info
short_description: Information module for networks _switch _stacks _routing _interfaces _dhcp
description:
- Get all networks _switch _stacks _routing _interfaces _dhcp.
- Return a layer 3 interface DHCP configuration for a switch stack.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
    - NetworkId path parameter. Network ID.
    type: str
  switchStackId:
    description:
    - SwitchStackId path parameter. Switch stack ID.
    type: str
  interfaceId:
    description:
    - InterfaceId path parameter. Interface ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for switch getNetworkSwitchStackRoutingInterfaceDhcp
  description: Complete reference of the getNetworkSwitchStackRoutingInterfaceDhcp API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp
notes:
  - SDK Method used are
    switch.Switch.get_network_switch_stack_routing_interface_dhcp,

  - Paths used are
    get /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp,
"""

EXAMPLES = r"""
- name: Get all networks _switch _stacks _routing _interfaces _dhcp
  cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    networkId: string
    switchStackId: string
    interfaceId: string
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample:
  - {}
"""
