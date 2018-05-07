from rest_framework import serializers
from .models import *

class MeetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetUser
        fields = ('Id','Token','FirstName',
                  'LastName','Email','PhoneNumber',
                  'Description','PhotoURL','Rating')

class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('Code')

class AgeRestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRestriction
        fields = ('MinAge','MaxAge')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('Id','EventName','TimeCreated','StartTime',
                  'EndTime','QrCode','CreatorId','GuestsIds','GuestsLimit',
                  'AgeRestriction','EventType','Latitude','Longitude',
                  'LocationName','Description','GoogleMapsURL')