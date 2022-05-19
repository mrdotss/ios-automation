from dataclasses import asdict
from pprint import pprint
import napalm


class OreNode():

    #Node info (change with your main)
    def __init__(self):
        self.node_ip = 'x.x.x.x'
        self.node_port = 22
        self.node_user = '#'
        self.node_pass = '#'
        self.node_secret = '#' #optional if you enable secret, add it to optional_args

    #Connecting the node
    def connectNode(self):

        try:
            print('Connecting to', self.node_ip, 'with port', self.node_port)

            # Use the IOS network driver to connect to the device
            driver = napalm.get_network_driver('ios')
            self.device = driver(hostname=self.node_ip, username=self.node_user,
                                password=self.node_pass, optional_args={'port': self.node_port, 'secret': self.node_secret})
            
            self.device.open()
            print('\nOpening..' + '\nStarting session..\n' + self.node_ip, 'is connected\n')
            
        except:
            print("\nConnecting failed!, something wrong. \nCommon causes: \n1. Incorret node info\n2. Firewall blocking the access")    


    # ARP Table
    def node_get_arp_table(self):
        try:
            print("\nARP Table List:")
            for item in self.device.get_arp_table():
                for scout_name, scout_value in item.items():
                    print(f" {scout_name}: {scout_value}")
                print()
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # BGP Config
    def node_get_bgp_config(self):
        try:
            if len(self.device.get_bgp_config()) != 0:
                print(self.device.get_bgp_config())
            else:
                print("\nBGP still not config yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # BGP Neighbors
    def node_get_bgp_neighbors(self):
        try:
            if len(self.device.get_bgp_neighbors()) != 0:
                print(self.device.get_bgp_neighbors())
            else:
                print("\nNo BGP Neighbors yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # BGP Neighbors Detail
    def node_get_bgp_neighbors_detail(self):
        try:
            if len(self.device.get_bgp_neighbors_detail()) != 0:
                print(self.device.get_bgp_neighbors_detail())
            else:
                print("\nNo BGP Neighbors detail yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # Show Config
    def node_get_config(self):
        try:
            for conf_key, conf_value in self.device.get_config().items():
                print(f"{conf_key}: {conf_value} ")
                print()
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # Show Condition Node
    def node_get_facts(self):
        try:
            print("Device Info:")
            for info_key, info_value in self.device.get_facts().items():
                print(f" {info_key}: {info_value}")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show Interface
    def node_get_interfaces(self):
        try:
            print("\nInfo about interfaces:")
            for key_interface, value_interface in self.device.get_interfaces().items():
                print(f"\nInterface {key_interface}")
                for info_interface, int_info in value_interface.items():
                    print(f"   {info_interface}: {int_info}")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # Show Interface Detail
    def node_get_interfaces_counters(self):
        try:
            def all_iface_counters():
                all_ct = 1
                all_iface_list = {}
                print("\nInterface status:")
                for iface_key_temp, value in self.device.get_interfaces_counters().items():
                    print(f"[{all_ct}] Interface: {iface_key_temp}")
                    all_iface_list[all_ct] = iface_key_temp
                    all_ct += 1
                    for ct_key, ct_value in value.items():
                        print(f"     {ct_key}: {ct_value}")
                    print()

            #Database and Count ID for interface list	
            ct = 1
            iface_list = {}
            for iface_ct, value in self.device.get_interfaces_counters().items():
                iface_list[ct] = iface_ct
                ct += 1

            #Print interface list
            ctr = 1
            print("\nInterface list:")
            for key_ex, value_temp in iface_list.items():
                print(f"{key_ex}. {value_temp}")
                ctr += 1
            print(f"{ctr}. All interface")

            ask = int(input("\nSelect interface: "))
            Pout = False

            #ID from api
            for iface_key, iface_value in self.device.get_interfaces_counters().items():
                #ID from iface_list data
                for key_temp, value_temp in iface_list.items():
                    #Finding interface as selected KEY
                    if ask == ct and not Pout:
                        all_iface_counters()
                        Pout = True
                        break		
                    elif value_temp == iface_key and iface_list[ask] == iface_key and ask == key_temp:
                        print(f"\nInterface: {iface_key}")
                        for ct_key, ct_value in iface_value.items():
                            print(f"  {ct_key}: {ct_value}")
                    elif ask+1 == ct + 1:
                        break
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show Interface IP
    def node_get_interfaces_ip(self):
        try:
            print("\nInfo about IP interfaces:")
            for key_interface, value_interface in self.device.get_interfaces_ip().items():
                print(f"\n{key_interface}")
                for ipv, ip_info in value_interface.items():
                    for ip, subnet in ip_info.items():
                        print(f" {ipv} - {ip}/{subnet['prefix_length']}")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show IPv6 Neighbors Table
    def node_get_ipv6_neighbors_table(self):
        try:
            if len(self.device.get_ipv6_neighbors_table()) != 0:
                print(self.device.get_bgp_neighbors())
            else:
                print("\nNo IPv6 Neighbors yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show LLDP Neightbors
    def node_get_lldp_neighbors(self):
        try:
            if len(self.device.get_lldp_neighbors()) != 0:
                print(self.device.get_lldp_neighbors())
            else:
                print("\nNo LLDP Neighbors yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # Show LLDP Neightbors Detail
    def node_get_lldp_neighbors_detail(self):
        try:
            if len(self.device.get_lldp_neighbors_detail()) != 0:
                print(self.device.get_lldp_neighbors_detail())
            else:
                print("\nNo LLDP Neighbors detail yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show MAC Table
    def node_get_mac_address_table(self):
        try:
            if len(self.device.get_mac_address_table()) != 0:
                print(self.device.get_mac_address_table())
            else:
                print("\nNo MAC address table yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show Instances Info
    def node_get_network_instances(self):
        try:
            for key, value in self.device.get_network_instances().items():
                print(f"{key}:")
                for key_item, key_value in value.items():
                    if key_item == 'state' or key_item == 'interfaces':
                        print(f"{key_item}:")
                        for k, v in key_value.items():
                            print(f"  {k}: {v}")
                        continue
                    print(f"{key_item}: {key_value}")        
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show NTP Peers
    def node_get_ntp_peers(self):
        try:
            if len(self.device.get_ntp_peers()) != 0:
                print(self.device.get_ntp_peers())
            else:
                print("\nNo NTP peer yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show NTP Servers
    def node_get_ntp_servers(self):
        try:
            if len(self.device.get_ntp_servers()) != 0:
                print(self.device.get_ntp_servers())
            else:
                print("\nNo NTP server yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show NTP Status
    def node_get_ntp_stats(self):
        try:
            if len(self.device.get_ntp_stats()) != 0:
                print(self.device.get_ntp_stats())
            else:
                print("\nNo NTP status yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show Optics
    def node_get_optics(self):
        try:
            print(self.device.get_optics())
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show Probes Config 
    def node_get_probes_config(self):
        try:
            print(self.device.get_probes_config())
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show SNMP Info
    def node_get_snmp_information(self):
        try:
            print("SNMP Info:")
            for key, value in self.device.get_snmp_information().items():
                print(f"{key}: {value}")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show User Info
    def node_get_users(self):
        try:
            for user_key, user_value in self.device.get_users().items():
                print(f"Username: {user_key}")
                for key, value in user_value.items():
                    print(f"{key}: {value}")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Show VLANs
    def node_get_vlans(self):
        try:
            if len(self.device.get_vlans()) != 0:
                print(self.device.get_vlans())
            else:
                print("\nNo VLAN are set yet.")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")

    # Check Node Status
    def node_is_alive(self):
        try:
            print("Node Status:")
            for key, value in self.device.is_alive().items():
                print("Status connection with", self.node_ip + " is", value)
                print("True: connected\nFalse: disconnected")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Test ICMP
    def node_ping(self):
        try:
            print("\nYou can input Hostname or IP address \nExample: 'google.com' or '10.x.x.x' (without quote)")
            dst = input("\nEnter your destination IP: ")
            print(f"\nPinging [{dst}] with 56 bytes of data:")
            for success, success_info in self.device.ping(dst, size=56).items():
                for key in success_info['results']:
                    print(f"Send to {key['ip_address']} rtt={key['rtt']}ms")
                    rec_probes = int(success_info['probes_sent'])
                    rec_loss = int(success_info['packet_loss'] / 20)
                    recv = abs(rec_loss - rec_probes)
                print(f"\nInfo packets send:\n   Sent: {success_info['probes_sent']}, Received: {recv}, Lost: {success_info['packet_loss']}%")
                print(f"RTT (round-trip delay) info:\n   Max: {success_info['rtt_max']}ms, Min: {success_info['rtt_min']}ms, Avg: {success_info['rtt_avg']}ms, StdDev: {success_info['rtt_stddev']}ms")
        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")
    
    # Traceroute
    def node_traceroute(self):
        try:
            pprint(self.device.ping('192.168.60.1'))
            pprint(self.device.traceroute('192.168.60.1'))
            print("\nHostname or IP address to trace\nExample: 'google.com' or '10.x.x.x' (without quote)")
            dst = input("\nEnter your destination IP: ")
            max_ttl = 0
            max_ttl = int(input("Enter Max HOP | MAX & Default=255: "))
            while max_ttl < 0 or max_ttl > 255 :
                print("Invalid MAX HOP!")
                max_ttl = int(input("\nEnter Max HOP | MAX & Default=255: "))
            print(f"\nTracing {dst} :")
            for trace_key, trace_value in self.device.traceroute(dst, ttl=max_ttl).items():
                for key, value in trace_value.items():
                    pprint(value['probes'])

        except SystemError as Err:
            self.device.close()
            print("Error", Err)
            print("\nDevice disconnected")