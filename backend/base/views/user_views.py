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
from base import serializers



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer= serializers.UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k]= v


        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):

    try:
        data = request.data
        user = User.objects.create(
            first_name=data['name'],
            username= data['email'],
            email=data['email'],
            password = make_password(data['password'])
        )
        serializer = serializers.UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message={'detail':'User with this email already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = serializers.UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data)