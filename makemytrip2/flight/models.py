from django.db import models

# Create your models here.
class FlightDetailsModel(models.Model):
    fname=models.CharField(max_length=25)
    fdate=models.DateField()
    ffare=models.FloatField()
    fstart=models.CharField(max_length=25)
    fend=models.CharField(max_length=25)