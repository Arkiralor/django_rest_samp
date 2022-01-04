from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serialized = ArticleSerializer(articles, many=True)
        return Response(serialized.data)

    elif request.method == 'POST':

        serialized = ArticleSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id:int):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = ArticleSerializer(article)
        return JsonResponse(serialized.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialized = ArticleSerializer(article, data=data)

        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serialized = ArticleSerializer(article)
        article.delete()
        return JsonResponse(serialized.data, status=status.HTTP_204_NO_CONTENT)