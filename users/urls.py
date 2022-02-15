from django.urls import path
from .views import Register, LoginView, UserView, LogoutView, TestApi, testApi2

urlpatterns = [
    path('register', Register.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('testapi', TestApi.as_view()),
    path('testapi2', testApi2),

]
