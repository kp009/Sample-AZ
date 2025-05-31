from rest_framework import serializers
from .models import Product  # or your model name

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
