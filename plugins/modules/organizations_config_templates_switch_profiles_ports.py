#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_config_templates_switch_profiles_ports
short_description: Resource module for organizations _configtemplates _switch _profiles _ports
description:
- Manage operation update of the resource organizations _configtemplates _switch _profiles _ports.
- Update a switch profile port.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  accessPolicyNumber:
    description: The number of a custom access policy to configure on the switch profile
      port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
    type: int
  accessPolicyType:
    description: The type of the access policy of the switch profile port. Only applicable
      to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list'
      or 'Sticky MAC allow list'.
    type: str
  allowedVlans:
    description: The VLANs allowed on the switch profile port. Only applicable to trunk
      ports.
    type: str
  configTemplateId:
    description: ConfigTemplateId path parameter. Config template ID.
    type: str
  daiTrusted:
    description: If true, ARP packets for this port will be considered trusted, and
      Dynamic ARP Inspection will allow the traffic.
    type: bool
  enabled:
    description: The status of the switch profile port.
    type: bool
  flexibleStackingEnabled:
    description: For supported switches (e.g. MS420/MS425), whether or not the port
      has flexible stacking enabled.
    type: bool
  isolationEnabled:
    description: The isolation status of the switch profile port.
    type: bool
  linkNegotiation:
    description: The link speed for the switch profile port.
    type: str
  macAllowList:
    description: Only devices with MAC addresses specified in this list will have access
      to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType'
      is 'MAC allow list'.
    elements: str
    type: list
  name:
    description: The name of the switch profile port.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  poeEnabled:
    description: The PoE status of the switch profile port.
    type: bool
  portId:
    description: PortId path parameter. Port ID.
    type: str
  portScheduleId:
    description: The ID of the port schedule. A value of null will clear the port schedule.
    type: str
  profile:
    description: Profile attributes.
    suboptions:
      enabled:
        description: When enabled, override this port's configuration with a port profile.
        type: bool
      id:
        description: When enabled, the ID of the port profile used to override the port's
          configuration.
        type: str
      iname:
        description: When enabled, the IName of the profile.
        type: str
    type: dict
  profileId:
    description: ProfileId path parameter. Profile ID.
    type: str
  rstpEnabled:
    description: The rapid spanning tree protocol status.
    type: bool
  stickyMacAllowList:
    description: The initial list of MAC addresses for sticky Mac allow list. Only applicable
      when 'accessPolicyType' is 'Sticky MAC allow list'.
    elements: str
    type: list
  stickyMacAllowListLimit:
    description: The maximum number of MAC addresses for sticky MAC allow list. Only
      applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
    type: int
  stormControlEnabled:
    description: The storm control status of the switch profile port.
    type: bool
  stpGuard:
    description: The state of the STP guard ('disabled', 'root guard', 'bpdu guard'
      or 'loop guard').
    type: str
  tags:
    description: The list of tags of the switch profile port.
    elements: str
    type: list
  type:
    description: The type of the switch profile port ('trunk' or 'access').
    type: str
  udld:
    description: The action to take when Unidirectional Link is detected (Alert only,
      Enforce). Default configuration is Alert only.
    type: str
  vlan:
    description: The VLAN of the switch profile port. A null value will clear the value
      set for trunk ports.
    type: int
  voiceVlan:
    description: The voice VLAN of the switch profile port. Only applicable to access
      ports.
    type: int
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for switch updateOrganizationConfigTemplateSwitchProfilePort
  description: Complete reference of the updateOrganizationConfigTemplateSwitchProfilePort API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port
notes:
  - SDK Method used are
    switch.Switch.update_organization_config_template_switch_profile_port,

  - Paths used are
    put /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.organizations_config_templates_switch_profiles_ports:
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
    accessPolicyNumber: 2
    accessPolicyType: Sticky MAC allow list
    allowedVlans: 1,3,5-10
    configTemplateId: string
    daiTrusted: false
    enabled: true
    flexibleStackingEnabled: true
    isolationEnabled: false
    linkNegotiation: Auto negotiate
    macAllowList:
    - 34:56:fe:ce:8e:b0
    - 34:56:fe:ce:8e:b1
    name: My switch port
    organizationId: string
    poeEnabled: true
    portId: string
    portScheduleId: '1234'
    profile:
      enabled: false
      id: '1284392014819'
      iname: iname
    profileId: string
    rstpEnabled: true
    stickyMacAllowList:
    - 34:56:fe:ce:8e:b0
    - 34:56:fe:ce:8e:b1
    stickyMacAllowListLimit: 5
    stormControlEnabled: true
    stpGuard: disabled
    tags:
    - tag1
    - tag2
    type: access
    udld: Alert only
    vlan: 10
    voiceVlan: 20

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "portId": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "enabled": true,
      "poeEnabled": true,
      "type": "string",
      "vlan": 0,
      "voiceVlan": 0,
      "allowedVlans": "string",
      "isolationEnabled": true,
      "rstpEnabled": true,
      "stpGuard": "string",
      "linkNegotiation": "string",
      "linkNegotiationCapabilities": [
        "string"
      ],
      "portScheduleId": "string",
      "udld": "string",
      "accessPolicyType": "string",
      "accessPolicyNumber": 0,
      "macAllowList": [
        "string"
      ],
      "stickyMacAllowList": [
        "string"
      ],
      "stickyMacAllowListLimit": 0,
      "stormControlEnabled": true,
      "flexibleStackingEnabled": true,
      "daiTrusted": true,
      "profile": {
        "enabled": true,
        "id": "string",
        "iname": "string"
      }
    }
"""
