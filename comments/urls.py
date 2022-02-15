from django.urls import path
from .views import CreateCommentApi, ViewCommentsApi

urlpatterns = [
    path('create/<str:post_id>', CreateCommentApi.as_view()),
    path('<str:post_id>', ViewCommentsApi.as_view()),
    
]
