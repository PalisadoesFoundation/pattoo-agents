# pattoo-snmpd

`pattoo-snmpd` provides performance data on any SNMP enabled system it can poll. The data gathered is posted in `json` format using HTTP to a remote server.

The `json` data is formatted for easy ingestion by [pattooDB](https://github.com/PalisadoesFoundation/pattoo-ng)

## Installation
The steps are simple.

* Install the required packages using the `pip_requirements` document in the root directory
```
$ sudo pip3 install -r pip_requirements.txt
```
* Populate the configuration files.
* Start the daemon.
* Add the daemons to `systemd` so they start on reboot. (TBD / Pending)

## Usage

`pattoo-snmpd` has a simple command structure.

The daemon will require a configuration file in the `etc/`directory. See the configuration section for details.

###
```bash
$ bin/pattoo-snmpd.py --help
usage: pattoo-snmpd.py [-h] [--start] [--stop] [--status] [--restart]
                         [--force]

optional arguments:
  -h, --help  show this help message and exit
  --start     Start the agent daemon.
  --stop      Stop the agent daemon.
  --status    Get daemon daemon status.
  --restart   Restart the agent daemon.
  --force     Stops or restarts the agent daemon ungracefully when used with --stop or
              --restart.
$
```

## Configuration

You will need to edit a configuration file in `etc/`directory. Pattoo will read any `.json` files found in this directory for configuration parameters.

For the sake of simplicity we will assume there is one file called `etc/config.yaml`

1. Make sure you have configured the `main` and `remote_api` sections of `etc/config.yaml` file before adding any sections for `pattoo-os` related daemons. The [CONFIGURATION.md](CONFIGURATION.md) file explains this in detail.
1. After doing this, edit the `etc/config.yaml` file to change configuration options specific to the daemons . An explanation follows.

### pattoo-snmpd Section

Add the following statements to the `config.yaml` file to configure the  `pattoo-snmpd` daemon. An explanation follows.


```yaml
pattoo-snmpd:

  oid_groups:
    - group_name: TEST
      ip_devices:
        - ip.address.of.device1
        - ip.address.of.device2
      oids:
        - .1.3.6.1.2.1.2.2.1.10
        - .1.3.6.1.2.1.2.2.1.16

  snmp_groups:
    - group_name: CISCO
      snmp_authpassword: null
      snmp_authprotocol: null
      snmp_community: public
      snmp_port: 161
      snmp_privpassword: null
      snmp_privprotocol: null
      snmp_secname: null
      snmp_version: 2
      ip_devices:
        - ip.address.of.device1
        - ip.address.of.device2
```

#### Configuration Explanation

This table outlines the purpose of each configuration parameter

|Section | Sub-Section |Config Options| Description|
|--|--|--|--|
|`pattoo-snmpd:`| | | **Note:** Only required for devices running `pattoo-snmpd` |
||`oid_groups:` || List of groupings of `ip_devices` that need data from a shared set of SNMP OIDs|
|||`group_name:`|Unique name for a group of `ip_devices` that share the same SNMP parameters|
|||`ip_devices:`| List of `ip_devices` to poll for OID data|
|||`oids:`| List of SNMP OIDs that we need data from for the `ip_devices`|
||`snmp_groups:` || List of groupings of `ip_devices` that share SNMP authentication parameters|
|||`group_name:`|Unique name for a group of `ip_devices` that share the same SNMP parameters|
|||`snmp_authpassword:`| SNMPv3 authpassword|
|||`snmp_authprotocol:`|SNMPv3 authprotocol|
|||`snmp_community:`|SNMPv2 community string|
|||`snmp_port:`|SNMP used by `ip_devices`|
|||`snmp_privpassword:`|SNMPv3 privpassword|
|||`snmp_privprotocol:`|SNMPv3 privprotocol|
|||`snmp_secname:`|SNMPv3 secname|
|||`snmp_version:`|SNMP version|
|||`ip_devices:`| List of `ip_addresses` or hostnmae to poll|


## Troubleshooting
Check the log files in the `log_directory` specified in your configuration.