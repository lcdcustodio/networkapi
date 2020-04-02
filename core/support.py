from ipaddress import *

class IpTools():

    def __init__(self):

        self.data = None

    def ipv4_check(self, address):

        self.data = False

        try:
            IPv4Network(address)
        except ValueError:
            self.data = True

        return self.data


    def cidr_check(self, address):

        self.data = False

        try:
            IPv4Network(address)
        except ValueError:
            self.data = True

        return self.data

    def subnet_range(self, address,subnet):

        self.data = False

        if address not in [str(ip) for ip in IPv4Network(subnet)]:
            self.data = True

        return self.data

    def ip_not_available(self, address,ip_pool):

        self.data = False

        for ip in ip_pool:

            if address == ip['ip_address']:
                self.data = True

        return self.data
