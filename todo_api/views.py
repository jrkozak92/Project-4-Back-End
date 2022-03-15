from django.shortcuts import render

from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
