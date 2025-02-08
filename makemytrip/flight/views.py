from django.shortcuts import render
from rest_framework.views import APIView
#to look good in froentend
from rest_framework.response import Response
#to create response in json
from rest_framework import status
#to return status
from .models import FlightDetailsModel
#model object
from .serilizers import FlightDetailsSer
#serilizers object

class Flight(APIView):
    def get(self,r):
        flightdetails=FlightDetailsModel.objects.all()
        serobj=FlightDetailsSer(flightdetails,many=True)
        #many=True to get all the data if we not insert it will return only 1 object
        return Response(serobj.data)

    def post(self,r):
        serobj=FlightDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class FlightUpdateDelete(APIView):
    def put(self,r,pk):
        #pk=primary key
        #ORM Query
        flightobj=FlightDetailsModel.objects.get(pk=pk)#data from request
        #convert above get data into Json and send to user
        serobj = FlightDetailsSer(flightobj,data=r.data)#data from client
        #mapping between flightobj & data=r.data
        #flightobj=database data,data=r.data=client data
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        flightobj = FlightDetailsModel.objects.get(pk=pk)
        flightobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






