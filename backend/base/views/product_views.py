from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base import models
from base import serializers
from rest_framework import status



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