from .models import User
import jwt

from django.http import JsonResponse


def auth_middleware(get_response):

    def auth_function(request):
        print(request.path)
        if request.path not in ['/admin/login', '/api/register', '/api/login']:

            # token = request.COOKIES.get('jwt')
            try:
                token = request.headers['Authorization'].replace('Bearer ', '')
            except:
                return JsonResponse({'detail': 'Unauthenticate!'}, status=401)
            # token = 1212
            # print(token)
            # if not token:
            #     return JsonResponse({'detail': 'Unauthenticate!'}, status=401)
            try:
                payload = jwt.decode(token, 'secret', algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return JsonResponse({'detail': 'Unauthenticate!'}, status=401)

            user = User.objects.filter(id=payload['id']).first()

            # if request.path != '/api/logout':
            # print(request.user)
            request.user_id = user.id
            # request.user = user
            # print(request.user)

        response = get_response(request)
        return response
    return auth_function
