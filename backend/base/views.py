from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


# Create your views here.

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
