# ios-automation

Automation for Cisco iOS<br>
What is dis? this project help you to use napalm package without too much coding, 
so you can just run the file and ready to command your MikroTik. Since this project used napalm-ros package, you can learn how to use the package.<br>

Note: You need to replace Node info with your own in `stuff/aho` module

### Getting started
first you need to install napalm packages

python 3.x</br>
`$ pip3 install napalm`<br>

### How to use
Change node info in `aho` module, then try uncomment code in base.py to use the function.<br>
`$ python3 base.py`

### Implemented getters works in this project
* get_arp_table
* get_bgp_config
* get_bgp_neighbors
* get_bgp_neighbors_detail
* get_config
* get_environment
* get_facts
* get_interfaces
* get_interfaces_counters
* get_interfaces_ip
* get_ipv6_neighbors_table
* get_lldp_neighbors
* get_lldp_neighbors_detail
* get_mac_address_table
* get_network_instances
* get_ntp_peers
* get_ntp_servers
* get_ntp_stats
* get_optics
* get_probes_config
* get_snmp_information
* get_users
* get_vlans
* is_alive
* ping
* traceroute