#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_firmware_upgrades_info
short_description: Information module for networks _firmwareupgrades
description:
- Get all networks _firmwareupgrades.
- Get firmware upgrade information for a network.
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
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for networks getNetworkFirmwareUpgrades
  description: Complete reference of the getNetworkFirmwareUpgrades API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades
notes:
  - SDK Method used are
    networks.Networks.get_network_firmware_upgrades,

  - Paths used are
    get /networks/{networkId}/firmwareUpgrades,
"""

EXAMPLES = r"""
- name: Get all networks _firmwareupgrades
  cisco.meraki.networks_firmware_upgrades_info:
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
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "upgradeWindow": {
        "dayOfWeek": "string",
        "hourOfDay": "string"
      },
      "timezone": "string",
      "products": {
        "wireless": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        },
        "appliance": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        },
        "switch": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        },
        "camera": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        },
        "cellularGateway": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        },
        "sensor": {
          "currentVersion": {
            "id": "string",
            "firmware": "string",
            "shortName": "string",
            "releaseType": "string",
            "releaseDate": "string"
          },
          "lastUpgrade": {
            "time": "string",
            "fromVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            },
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "nextUpgrade": {
            "time": "string",
            "toVersion": {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          },
          "availableVersions": [
            {
              "id": "string",
              "firmware": "string",
              "shortName": "string",
              "releaseType": "string",
              "releaseDate": "string"
            }
          ],
          "participateInNextBetaRelease": true
        }
      }
    }
"""
