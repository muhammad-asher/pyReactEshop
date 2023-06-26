from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from base import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base import models


def getroutes(request):
    routes = [
        '/api/products',
        '/api/products/create',

        '/api/products/uploads/',

        '/api/products/<id>/reviews',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>',
        '/api/products/<update>/<id>',
    ]
    return JsonResponse(routes, safe=False)

