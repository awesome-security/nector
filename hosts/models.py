from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    """Model for individual hosts, consisting of an ip and a hostname"""
    ipv4_address = models.GenericIPAddressField(protocol='ipv4', default='0.0.0.0')
    host_name = models.CharField(max_length=80)

    def __str__(self):
        return "%s, %s" % (self.ipv4_address, self.host_name)

class Subnet(models.Model):
    """Model for subnets, consisting of an ip address and a network prefix"""
    ipv4_address = models.GenericIPAddressField(protocol='ipv4', default='0.0.0.0')
    prefix = models.IntegerField()

    def __str__(self):
        return "%s/%s" % (self.ipv4_address, self.prefix)