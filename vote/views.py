from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import Vote
from .serializers import VoteSerializer


# Create your views here.
class giveVote(APIView):

    def post(self, request, post_id):

        already_voted = Vote.objects.filter(Q(author__id=request.user_id) & 
                                            Q(post__id=post_id))
        if(already_voted):
            print(already_voted[0])
            return Response({'id':already_voted[0].id, 'mgs': 'Already voted'})
        

        vote = request.data
        vote['author'] = request.user_id
        vote['post'] = post_id
        serializer = VoteSerializer(data=vote)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class viewVote(APIView):

    def get(self, request, post_id):
        positive_vote = Vote.objects.filter(Q(reaction=1) & Q(post__id=post_id)).count()

        negative_vote = Vote.objects.filter(Q(reaction=0) & Q(post__id=post_id)).count()

        return Response({'positive_vote': positive_vote, 'negative_vote': negative_vote})


class removeVote(APIView):

    def delete(self, request, pk):
        vote = Vote.objects.get(id=pk)
        vote.delete()

        return Response({'mgs':'vote remove successfully'})
