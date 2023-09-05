#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_traffic_analysis
short_description: Resource module for networks _trafficanalysis
description:
- Manage operation update of the resource networks _trafficanalysis.
- Update the traffic analysis settings for a network.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  customPieChartItems:
    description: The list of items that make up the custom pie chart for traffic reporting.
    elements: dict
    suboptions:
      name:
        description: The name of the custom pie chart item.
        type: str
      type:
        description: The signature type for the custom pie chart item. Can be one of
          'host', 'port' or 'ipRange'.
        type: str
      value:
        description: The value of the custom pie chart item. Valid syntax depends on
          the signature type of the chart item (see sample request/response for more
          details).
        type: str
    type: list
  mode:
    description: The traffic analysis mode for the network. Can be one of 'disabled'
      (do not collect traffic types), 'basic' (collect generic traffic categories),
      or 'detailed' (collect destination hostnames).
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for networks updateNetworkTrafficAnalysis
  description: Complete reference of the updateNetworkTrafficAnalysis API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis
notes:
  - SDK Method used are
    networks.Networks.update_network_traffic_analysis,

  - Paths used are
    put /networks/{networkId}/trafficAnalysis,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_traffic_analysis:
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
    state: present
    customPieChartItems:
    - name: Item from hostname
      type: host
      value: example.com
    - name: Item from port
      type: port
      value: '440'
    - name: Item from IP
      type: ipRange
      value: 192.1.0.0
    - name: Item from IP range (CIDR)
      type: ipRange
      value: 192.2.0.0/16
    - name: Item from IP range with port
      type: ipRange
      value: 192.3.0.0/16:80
    mode: detailed
    networkId: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
