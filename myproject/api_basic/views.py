from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response

# Create your views here.

def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serialized = ArticleSerializer(articles, many=True)
        return JsonResponse(serialized.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = ArticleSerializer(data=data)

        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status=201)
        else:
            return JsonResponse(serialized.errors, status=400)


