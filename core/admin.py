from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import IpAddress

admin.site.unregister(User)
admin.site.unregister(Group)


class IpAddressAdmin(ModelAdmin):
    list_display = ('ip_address', 'subnet', 'description')

admin.site.register(IpAddress, IpAddressAdmin)


