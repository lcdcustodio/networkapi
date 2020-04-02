from django.test import TestCase
from core.models import IpAddress
from core.support import IpTools

class IpAddressTest(TestCase):

    def setUp(self):

        self.ip_address="192.1.1.1"
        self.subnet = "192.1.1.0/24"
        self.description="TestCase_model"
        self.ip_conflict = "192.1.1.0"
        self.ipv4 = "192.1.1.1"

    def create_ipaddress(self):

        return IpAddress.objects.create(ip_address=self.ip_address, subnet=self.subnet, description=self.description)


    def test_ipaddress_creation(self):

        ip_model = self.create_ipaddress()
        self.assertTrue(isinstance(ip_model, IpAddress))
        self.assertEqual(ip_model.__str__(), ip_model.ip_address)


    def test_subnet_notation(self):

        subnet_issue = IpTools().cidr_check(self.subnet)
        self.assertEqual(subnet_issue, False)

    def test_ipv4_check(self):

        subnet_issue = IpTools().ipv4_check(self.ipv4)
        self.assertEqual(subnet_issue, False)


    def test_subnet_range(self):

        subnet_range_issue = IpTools().subnet_range(self.ip_address, self.subnet)
        self.assertEqual(subnet_range_issue, False)

    def test_ip_availabilty(self):

        IpAddress.objects.create(ip_address=self.ip_address, subnet=self.subnet, description=self.description)
        ip_pool = IpAddress.objects.all().values()

        ip_used = IpTools().ip_not_available(self.ip_conflict, ip_pool)

        self.assertEqual(ip_used, False)
