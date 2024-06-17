from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView


# Create your views here.
class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreate(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieve(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdate(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDestroy(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDelete(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
