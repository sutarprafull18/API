from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FlightDetailsModel
from .serializers import FlightDetailsSer
# Create your views here.

class Flight(APIView):
    def get(self, request):
        flightdeatils = FlightDetailsModel.objects.all()
        serobj = FlightDetailsSer(flightdeatils, many=True)
        return  Response(serobj.data)

    def post(self, request):
        serobj = FlightDetailsSer(data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

class FlightUpdateDelete(APIView):
    def put(self,r,pk):
        flightobj = FlightDetailsModel.objects.get(pk=pk)
        serobj = FlightDetailsSer(flightobj, data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, r, pk):
        flightobj = FlightDetailsModel.objects.get(pk=pk)
        flightobj.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
