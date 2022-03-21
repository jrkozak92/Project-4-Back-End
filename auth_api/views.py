from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def check_login(request):
    if request.method == 'GET':
        return JsonResponse({})
    if request.method == 'PUT':
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']

        if User.objects.filter(username=username):
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'username': user.username, 'password': user.password, 'list_names': user.list_names,})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})

def add_list(request):
    if request.method == 'PUT':
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        list_names = jsonRequest['list_names']

        if User.objects.filter(username=username):
            user = User.objects.get(username=username)
            user.list_names = list_names
            user.save()
            return JsonResponse({'username': user.username, 'list_names': user.list_names})
        else:
            return JsonResponse({})
