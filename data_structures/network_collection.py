from ipaddress import IPv4Network, IPv4Address
class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        ipv4_network = IPv4Network(ipv4_network)
        self.ipv4_network = ipv4_network
        self.entries = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        import re
        ok_networks = []
        regex = "^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$"

        for i in self.entries:
            ip_address = i['address']
            # treats IP as a subnet e.g /32
            # check if /32 is part of the network - return True
            if re.search(regex, ip_address) and IPv4Network(ip_address).subnet_of(self.ipv4_network):
                ok_networks.append(i)
        return ok_networks



    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
