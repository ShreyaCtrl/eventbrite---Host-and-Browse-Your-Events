from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/events/',
            'method': 'GET',
            "body": None,
            'description': 'Returns an array of events.'
        },
        {
            'Endpoint': '/events/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single event object.'
        },
        {
            'Endpoint': '/events/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new event with data sent in post request.'
        },
        {
            'Endpoint': '/events/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing event with data sent in post request.'
        },
    ]
    return response.Response(routes)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def getEvents(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(events, many=False)
    return response.Response(serializer.data)