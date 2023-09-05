#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_adaptive_policy_acls_info
short_description: Information module for organizations _adaptivepolicy _acls
description:
- Get all organizations _adaptivepolicy _acls.
- Get organizations _adaptivepolicy _acls by id.
- List adaptive policy ACLs in a organization.
- Returns the adaptive policy ACL information.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
    - OrganizationId path parameter. Organization ID.
    type: str
  aclId:
    description:
    - AclId path parameter. Acl ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for organizations getOrganizationAdaptivePolicyAcl
  description: Complete reference of the getOrganizationAdaptivePolicyAcl API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl
- name: Cisco Meraki documentation for organizations getOrganizationAdaptivePolicyAcls
  description: Complete reference of the getOrganizationAdaptivePolicyAcls API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_adaptive_policy_acl,
    organizations.Organizations.get_organization_adaptive_policy_acls,

  - Paths used are
    get /organizations/{organizationId}/adaptivePolicy/acls,
    get /organizations/{organizationId}/adaptivePolicy/acls/{aclId},
"""

EXAMPLES = r"""
- name: Get all organizations _adaptivepolicy _acls
  cisco.meraki.organizations_adaptive_policy_acls_info:
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
    organizationId: string
  register: result

- name: Get organizations _adaptivepolicy _acls by id
  cisco.meraki.organizations_adaptive_policy_acls_info:
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
    organizationId: string
    aclId: string
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "aclId": "string",
      "name": "string",
      "description": "string",
      "ipVersion": "string",
      "rules": [
        {
          "policy": "string",
          "protocol": "string",
          "srcPort": "string",
          "dstPort": "string"
        }
      ],
      "createdAt": "string",
      "updatedAt": "string"
    }
"""
