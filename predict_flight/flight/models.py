from django.db import models

# Create your models here.


class Flight(models.Model):
    airline = models.CharField(max_length=24, null=False, default='Airline')
    date_of_journey = models.DateTimeField(auto_now_add=False, null=False)
    source = models.CharField(max_length=16, null=False, default='Source')
    destination = models.CharField(max_length=16, null=False, default='Destination')
    route = models.CharField(max_length=256, blank=True, null=True)
    dep_time = models.CharField(max_length=5, null=False, default='00:00')
    arrival_time = models.CharField(max_length=5, null=False, default='00:00')
    duration = models.CharField(max_length=16, null=False, default='0h 0m')
    total_stops = models.CharField(max_length=16, null=False, default='non-stop')
    additional_info = models.CharField(max_length=16, blank=True, default='No info')