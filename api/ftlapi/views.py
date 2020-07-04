from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ActivitySerializer, UserSerializer
from .models import User, Activity



@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activityList(request):
    activity = User.objects.all()
    serializer = ActivitySerializer(activity, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def activityCreate(request):    
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
