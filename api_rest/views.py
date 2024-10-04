from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET']) #verifica a função do tipo GET
def get_users(request): #retorna dados em formato apropriado

    if request.method =='GET':

        users= User.objects.all() #recupera todas infos do BD que correspondem a User e armazena na variavel users

        serializer= UserSerializer(users, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_NOT_FOUND) #respostas dos dados serializados (json)

# def databaseEmDjango():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()

