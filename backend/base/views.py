from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .products import products
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from . import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models
from . import serializers


# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer= serializers.UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k]= v


        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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

@api_view(['GET'])
def getProducts(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = models.Product.objects.get(_id=pk)
    serializer = serializers.ProductSerializer(product, many=False)
    return Response(serializer.data)


    # product = None
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    #
    # return Response(product)
