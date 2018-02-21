from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'identifier')


class EmisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emisor
        fields = ('name', 'identifier')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmisorViewSet(viewsets.ModelViewSet):
    queryset = Emisor.objects.all()
    serializer_class = EmisorSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'comercios', CompanyViewSet)
router.register(r'emisores', EmisorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
