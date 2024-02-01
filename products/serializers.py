from rest_framework import serializers
from dataclasses import field
from pyexpat import model
from urllib import request, response
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model



# # //product serializers
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        depth=1
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth=1


