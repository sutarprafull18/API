from rest_framework import serializers
from .models import FlightDetailsModel

class FlightDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = FlightDetailsModel
        fields = '__all__'