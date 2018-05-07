from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class Events(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = ()

class MeetUsers(viewsets.ModelViewSet):
    queryset = MeetUser.objects.all()
    serializer_class = MeetUserSerializer
    permission_classes = ()
