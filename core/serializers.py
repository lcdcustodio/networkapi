from django.contrib.auth.models import User
from rest_framework import serializers
from .models import IpAddress

# Serializers define the API representation.
class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ['id', 'ip_address','subnet', 'description']
