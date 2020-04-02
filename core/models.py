from django.db import models
from ipaddress import *
from django.core.exceptions import ValidationError
from .support import IpTools

class IpAddress(models.Model):

    ip_address = models.GenericIPAddressField(help_text=('IPv4 only'))

    #ip_address = models.GenericIPAddressField(protocol='IPv4',
    #                      help_text=('IPv4 only'))


    subnet = models.CharField(max_length=100, blank=False,
                          help_text=('Subnet in CIDR notation, e.g.: "10.0.0.0/24" - IPv4 only'))
    description = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.ip_address


    def clean(self, *args, **kwargs):
        # add custom validation here
        super(IpAddress, self).clean(*args, **kwargs)
        """
        try:
            IPv4Network(self.subnet)
        except:
            raise ValidationError({
                'subnet': ('Invalid subnet notation')
            })
        """
        ipv4_check = IpTools().cidr_check(self.ip_address)

        if ipv4_check:
            raise ValidationError({
                'ip_address': ('Invalid IPv4 notation')
            })


        subnet_issue = IpTools().cidr_check(self.subnet)

        if subnet_issue:
            raise ValidationError({
                'subnet': ('Invalid subnet notation')
            })
        """
        if self.ip_address not in [str(ip) for ip in IPv4Network(self.subnet)]:
            raise ValidationError({
                'ip_address': ('IP address does not belong to the subnet')
            })
        """

        subnet_range_issue = IpTools().subnet_range(self.ip_address, self.subnet)

        if subnet_range_issue:
            raise ValidationError({
                'ip_address': ('IP address does not belong to the subnet')
            })

        addresses = IpAddress.objects.all().values()

        ip_used = IpTools().ip_not_available(self.ip_address, addresses)

        if ip_used:
            raise ValidationError({
                'ip_address': ('IP address already used.')
            })

        """
        addresses = IpAddress.objects.all().values()
        for ip in addresses:

            if self.ip_address == ip['ip_address']:
                raise ValidationError({
                    'ip_address': ('IP address already used.')
                })
        """

