from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
