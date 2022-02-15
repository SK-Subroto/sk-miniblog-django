from .models import User
import jwt
from rest_framework.decorators import api_view

from django.http import HttpResponse


def authenticate(view_func):
    def wrapper_func(request, *args, **kwargs):

        print(request.COOKIES['jwt'])
        return view_func(request, *args, **kwargs)

    return wrapper_func
