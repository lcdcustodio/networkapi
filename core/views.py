from rest_framework import viewsets, status
from rest_framework.decorators import action
from ipaddress import *
from .models import IpAddress
from .serializers import IpAddressSerializer
from rest_framework.response import Response
from .support import IpTools

class IpAddressViewSet(viewsets.ModelViewSet):

    serializer_class = IpAddressSerializer

    def get_queryset(self):
        ip_x = self.request.query_params.get('ip_address')
        queryset = IpAddress.objects.all()

        if ip_x:
            queryset = IpAddress.objects.filter(ip_address=ip_x)

        return queryset

    def create(self, request, *args, **kwargs):

        return Response({'status': 'access denied'})

    def destroy(self, request, *args, **kwargs):

        try:
            ip_del = IpAddress.objects.get(pk=kwargs['pk'])

        except IpAddress.DoesNotExist:
            return Response({'error': 'IP_id does not exist'})

        operation = ip_del.delete()
        data = {}
        if operation:
            data['status'] = "delete successful"
        else:
            data['status'] = "delete failed"

        return Response(data=data)



    @action(detail=False, methods=['POST'])
    def new(self, request):

        ipv4_check = IpTools().cidr_check(request.data['ip_address'])

        if ipv4_check:
            return Response({'error': 'Invalid IPv4 notation'})

        subnet_issue = IpTools().cidr_check(request.data['subnet'])

        if subnet_issue:
            return Response({'error': 'Invalid subnet notation'})

        subnet_range_issue = IpTools().subnet_range(request.data['ip_address'], request.data['subnet'])

        if subnet_range_issue:
            return Response({'error': 'IP does not belong to the subnet'})

        addresses = IpAddress.objects.all().values()

        ip_used = IpTools().ip_not_available(request.data['ip_address'], addresses)

        if ip_used:
            return Response({'error': 'IP address already used'})


        serializer = IpAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','info' : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

