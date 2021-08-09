from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer2,SongSerializer
from .models import Songs

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        "List":"/list/",
        "Detail of 1 particular song":"/detail/<str:pk>",
        "Create":"/create/"
    }
    return Response(api_urls)

@api_view(['GET'])
def lists(request):
    lists = Songs.objects.all().order_by('name')
    serializer = SongSerializer2(lists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def details(request):
    id=request.GET.get('id')
    genre=request.GET.get('genre')
    singer=request.GET.get('singer')
    name=request.GET.get('name')
    if id:
        details = details.get(id=id)
        serializer = SongSerializer(details)
        return Response(serializer.data)
    details=Songs.objects.all()
    if singer:
        details = details.filter(singer=singer)
    if name:
        details = details.filter(name=name)
    if genre:
        details = details.filter(genre=genre)
    
    serializer = SongSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

