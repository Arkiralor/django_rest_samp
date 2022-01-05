from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializerRep, StudentSerializerInp
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serialized = StudentSerializerRep(students, many=True)
    return Response(serialized.data)


@api_view(['POST'])
def add_student(request):
    serialized = StudentSerializerInp(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_id(request, id: int):
    try:
        student = Student.objects.get(id=id)
        serialized = StudentSerializerRep(student)
        return Response(serialized.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_student(request, id: int):
    try:
        student = Student.objects.get(id=id)
        data = request.data
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialized = StudentSerializerInp(student, data=data)

    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_student(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized = StudentSerializerRep(student)
    student.delete()
    return Response(serialized.data, status=status.HTTP_410_GONE)
