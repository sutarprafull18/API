from rest_framework import serializers
from .models import FlightDetailsModel

class FlightDetailsSer(serializers.ModelSerializer):
    class Meta:
        model=FlightDetailsModel
        fields="__all__"

#This is used to convert data
# 1.Recieved format data to json
# 2.Json to Expected format of data(here python)