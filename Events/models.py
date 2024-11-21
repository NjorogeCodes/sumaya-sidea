from django.db import models
from timezone_field import TimeZoneField


# Create your models here.




class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="0")
    start_time = models.DateTimeField(default=TimeZoneField)
    end_time = models.DateTimeField(default=TimeZoneField)
    price = models.IntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    organizer = models.CharField(max_length=100)
    timezone = TimeZoneField(default='UTC')
    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100, default="0")
    Event=models.ForeignKey(to=Event,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

