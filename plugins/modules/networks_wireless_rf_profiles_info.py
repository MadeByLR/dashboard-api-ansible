#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_wireless_rf_profiles_info
short_description: Information module for networks _wireless _rfprofiles
description:
- Get all networks _wireless _rfprofiles.
- Get networks _wireless _rfprofiles by id.
- List the non-basic RF profiles for this network.
- Return a RF profile.
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
  includeTemplateProfiles:
    description:
    - >
      IncludeTemplateProfiles query parameter. If the network is bound to a template, this parameter controls
      whether or not the non-basic RF profiles defined on the template should be included in the response
      alongside the non-basic profiles defined on the bound network. Defaults to false.
    type: bool
  rfProfileId:
    description:
    - RfProfileId path parameter. Rf profile ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for wireless getNetworkWirelessRfProfile
  description: Complete reference of the getNetworkWirelessRfProfile API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile
- name: Cisco Meraki documentation for wireless getNetworkWirelessRfProfiles
  description: Complete reference of the getNetworkWirelessRfProfiles API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_network_wireless_rf_profile,
    wireless.Wireless.get_network_wireless_rf_profiles,

  - Paths used are
    get /networks/{networkId}/wireless/rfProfiles,
    get /networks/{networkId}/wireless/rfProfiles/{rfProfileId},
"""

EXAMPLES = r"""
- name: Get all networks _wireless _rfprofiles
  cisco.meraki.networks_wireless_rf_profiles_info:
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
    includeTemplateProfiles: True
    networkId: string
  register: result

- name: Get networks _wireless _rfprofiles by id
  cisco.meraki.networks_wireless_rf_profiles_info:
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
    rfProfileId: string
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {}
    ]
"""
