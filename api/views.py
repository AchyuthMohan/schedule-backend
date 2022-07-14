from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from .serializers import TodoSerializer
# Create your views here.

@api_view(['GET','POST'])
def todo_list(request):
    if request.method=='GET':
        Todos=Todo.objects.all()
        serializer=TodoSerializer(Todos,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def todo_detail(request,pk):
    try:
        Todo=Todo.objects.get(pk=pk)

    except Todo.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=TodoSerializer(Todo)
        return Response(serializer.data)

    elif request.method=="PUT":
        serializer=TodoSerializer(Todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        Todo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)