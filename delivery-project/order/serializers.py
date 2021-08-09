from rest_framework import serializers
from .models import Orders, BoyDetails

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('ordername','orderaddress','orderstatus','deliveryboy')

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoyDetails
        fields = ('boyname','phone','boystatus')