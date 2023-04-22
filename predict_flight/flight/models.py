from django.db import models

# Create your models here.

class Flight(models.Model):
    airline = models.CharField(max_length=36, default='Airline', null=False)
    flight_date = models.DateField(auto_now_add=True, null=False)
    source = models.CharField(max_length=20, default='City', null=False)
    destination = models.CharField(max_length=20, default='City', null=False)
    route = models.CharField(max_length=256, blank=True, null=True)
    dep_time = models.TimeField(auto_now_add=True, null=False)
    arrival_time = models.TimeField(auto_now_add=True, null=False)
    duration = models.TimeField(auto_now_add=True, null=False)
    total_stops = models.CharField(max_length=16, null=False, default='non-stop')
    additional_info = models.CharField(max_length=36, null=False, default='No info')
