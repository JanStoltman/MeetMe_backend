from django.db import models

# Create your models here
# Leave capital letter for the compatibility sake.
class MeetUser(models.Model):
    Id = models.AutoField(primary_key=True)
    Token = models.TextField(default="")
    FirstName = models.TextField(default="")
    LastName = models.TextField(default="")
    Email = models.EmailField(default="")
    PhoneNumber = models.TextField(default="")
    Description = models.TextField(default="")
    PhotoURL = models.TextField(default="")
    Rating = models.DecimalField(default=3.0, decimal_places=10, max_digits=20)

class QrCode(models.Model):
    Code = models.TextField(default="")

class AgeRestriction(models.Model):
    MinAge = models.IntegerField(default=1)
    MaxAge = models.IntegerField(default=99)

EVENT_TYPE = (
    (0, 'PublicEvent'),
    (1, 'PrivateEvent'),
)

class Event(models.Model):
    Id = models.AutoField(primary_key=True)
    EventName = models.TextField(default="")
    TimeCreated = models.BigIntegerField(default=0)
    StartTime =models.BigIntegerField(default=0)
    EndTime = models.BigIntegerField(default=0)
    QrCode = models.ForeignKey(QrCode, on_delete=models.CASCADE)
    CreatorId = models.ForeignKey(MeetUser, on_delete=models.DO_NOTHING, related_name="creator_of")
    GuestsIds = models.ManyToManyField(MeetUser, related_name="guest_of")
    GuestsLimit = models.IntegerField(default=4)
    AgeRestriction = models.ForeignKey(AgeRestriction, on_delete=models.DO_NOTHING)
    EventType = models.IntegerField(default=0, choices=EVENT_TYPE)
    Latitude = models.DecimalField(default=0.0, decimal_places=10, max_digits=20)
    Longitude = models.DecimalField(default=0.0, decimal_places=10, max_digits=20)
    LocationName = models.TextField(default="")
    Description = models.TextField(default=0.0)
    GoogleMapsURL = models.TextField(default=0.0)
