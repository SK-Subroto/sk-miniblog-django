from django.urls import path
from .views import giveVote, removeVote, viewVote

urlpatterns = [
    path('give/<str:post_id>', giveVote.as_view()),
    path('remove-vote/<str:pk>', removeVote.as_view()),
    path('<str:post_id>', viewVote.as_view()),
]
