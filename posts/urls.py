from django.urls import path
from .views import CreatePostApi, ViewPostApi, ViewPostByIdApi

urlpatterns = [
    path('create', CreatePostApi.as_view()),
    path('', ViewPostApi.as_view()),
    path('<str:pk>', ViewPostByIdApi.as_view())
]
