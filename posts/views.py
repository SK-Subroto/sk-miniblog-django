from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post
from .serializers import PostSerializer
from users.models import User

# Create your views here.
class CreatePostApi(APIView):

    def post(self, request):
        
        post = request.data
        post['author'] = request.user_id
        # post['author'] = 3
        print(request.user)
        serializer = PostSerializer(data=post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        return Response({
            "data": "success"
        })


class ViewPostApi(APIView):

    def get(self, request):

        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class ViewPostByIdApi(APIView):
    # authentication_classes = [ JWTAuthentication ]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
