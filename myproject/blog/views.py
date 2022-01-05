from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
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


class PostView(APIView):
    def get(self, request, id: int):
        try:
            post = Blog.objects.get(id=id)
            serialized = BlogSerializer(post)
            return Response(serialized.data, status=status.HTTP_302_FOUND)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id: int):
        try:
            bpost = Blog.objects.get(id=id)
            data = request.data
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized = BlogSerializer(bpost, data=data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id: int):
        try:
            bpost = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized = BlogSerializer(bpost)
        bpost.delete()
        return Response(serialized.data, status=status.HTTP_410_GONE)
