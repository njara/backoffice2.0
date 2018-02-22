from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.response import Response

from .serializers import *


class CompanyList(APIView):
    """
    Get the Company from Transbank DB.
    """

    def get(self, request, format=None):
        issuers = Company.objects.all()

        serializer = CompanySerializer(issuers, many=True,)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #if not request.auth:
            # only allowed from mobile app
         #   return Response(status=status.HTTP_403_FORBIDDEN)

            # include infield user in request
            # if request.data:
            #     request.data._mutable = True
            #    request.data['infield_user'] = request.user
            #   request.data._mutable = False
            #   serializer = IssusingSerializer(data=request.data)
            # else:
            #   serializer = IssusingSerializer(data={'infield_user': request.user})
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssusingList(APIView):
    """
    Get the Issuers from Transbank DB.
    """

    def get(self, request, format=None):
        issuers = Emisor.objects.all()

        serializer = IssusingSerializer(issuers, many=True,)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #if not request.auth:
            # only allowed from mobile app
         #   return Response(status=status.HTTP_403_FORBIDDEN)

            # include infield user in request
            # if request.data:
            #     request.data._mutable = True
            #    request.data['infield_user'] = request.user
            #   request.data._mutable = False
            #   serializer = IssusingSerializer(data=request.data)
            # else:
            #   serializer = IssusingSerializer(data={'infield_user': request.user})
        serializer = IssusingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileList(APIView):
    """
    Get the UserProfile from Transbank DB.
    """

    def get(self, request, format=None):
        users = UserProfile.objects.all()

        serializer = UserProfileSerializer(users, many=True,)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #if not request.auth:
            # only allowed from mobile app
         #   return Response(status=status.HTTP_403_FORBIDDEN)

            # include infield user in request
            # if request.data:
            #     request.data._mutable = True
            #    request.data['infield_user'] = request.user
            #   request.data._mutable = False
            #   serializer = IssusingSerializer(data=request.data)
            # else:
            #   serializer = IssusingSerializer(data={'infield_user': request.user})
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
