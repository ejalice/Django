from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from user.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Create your views here.


'''
user = authenticate(request, username=username, password = password)
if user is not None:
    login(request ,user)
'''

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # user = serializer.save()      
            user = serializer.create(serializer.validated_data)

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    'user': serializer.data,
                    'message': 'register success',
                    'token': {
                        'access': access_token,
                        'refresh': refresh_token
                    },
                },
                status = status.HTTP_200_OK,
            )
            return res
        else:
            print("Register - Not Valid")
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AuthView(APIView):

    def post(self, request):
        user = authenticate (
            email = request.data.get('email'),
            password = request.data.get('password')
        )

        if user is not None:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": 'register success',
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(
                {"해당 User가 없습니다."}, status=status.HTTP_400_BAD_REQUEST
            )