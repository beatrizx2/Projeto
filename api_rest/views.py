from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User

import json

@api.view(['GET'])
def get_users(request):

    if request.method =='GET':

        users= User.objects.GET()

        serializer= UserSerializer(users, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_NOT_FOUND)

# def databaseEmDjango():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()

