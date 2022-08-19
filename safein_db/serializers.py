# product/serializers.py
from rest_framework import serializers
from .models import *


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel        
        fields = '__all__'     


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'          
        
        
        
class EnrollerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroller
        fields = '__all__'            # 모든 필드 포함


