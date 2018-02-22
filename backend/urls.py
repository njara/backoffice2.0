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

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^companies/', CompanyList.as_view(), name='companies'),
    url(r'^issuers/', IssusingList.as_view(), name='issuers'),
    url(r'^users/', UserProfileList.as_view(), name='users'),
]
