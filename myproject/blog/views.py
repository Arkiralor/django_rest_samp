from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class BlogAPIView(APIView):
    def get(self, request):
        posts = Blog.objects.all()
        serialized = BlogSerializer(posts, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = BlogSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)