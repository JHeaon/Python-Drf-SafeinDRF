from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    
class EnrollerViewSet(viewsets.ModelViewSet):
    queryset = Enroller.objects.all()
    serializer_class = EnrollerSerializer    