from django.db import models

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=100)
    Flight_number = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    food_service = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.IntegerField()
    status = models.CharField(max_length=100)
    
    
