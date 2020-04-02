from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import IpAddressViewSet


admin.site.site_header = "Network Administration"
admin.site.site_title = "Network Administration Portal"
admin.site.index_title = "Network Administration Portal"

router = routers.DefaultRouter()
router.register('network', IpAddressViewSet, basename='network')


#app_name = 'netapi'

urlpatterns = [

    path('api/v1/', include((router.urls,'api'),namespace='api')),
    #path('api/v1/', include(router.urls,)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
