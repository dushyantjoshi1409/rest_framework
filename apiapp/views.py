from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request,id = 0):
    if request.method == 'GET':
        flights = Flight.objects.all()
        new_data = FlightSerializer(flights, many=True)
        return JsonResponse(new_data.data, safe=False)
    
    elif request.method == 'POST':
        flights = JSONParser().parse(request)
        flight_serializer = FlightSerializer(data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("data added succesfully", safe=False)
        return JsonResponse("data not added succesfully", safe=False)

    elif request.method == 'PUT':
        flights = JSONParser().parse(request)
        flight_data = Flight.objects.get(id=flights['id'])
        flight_serializer = FlightSerializer(flight_data, data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("data updated succesfully", safe=False)
        return JsonResponse("data not updated succesfully", safe=False)

    elif request.method == 'DELETE':
        flight_data = Flight.objects.get(id=id)
        flight_data.delete()
        return JsonResponse("data deleted succesfully", safe=False)