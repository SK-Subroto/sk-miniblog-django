from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer
from users.models import User

# Create your views here.
class CreateCommentApi(APIView):
    
    def post(self, request, post_id):

        comment = request.data
        comment['author'] = request.user_id
        comment['post'] = post_id
        serializer = CommentSerializer(data=comment)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ViewCommentsApi(APIView):

    def get(self, request, post_id):
        
        comments = Comment.objects.filter(post__id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
