from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login, logout,get_user_model
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from .serializers import *
from django.utils import timezone
from django.db import IntegrityError
from rest_framework import generics


@requires_csrf_token
@api_view(['POST'])
def login_user(request, format=None):
    try:
        if request.user.is_authenticated:
            return Response(status = status.HTTP_200_OK)
       
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        Response(errors = serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_up(request, format=None):
    if request.user.is_authenticated:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    try:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            name = serializer.validated_data["name"]
            bio = serializer.validated_data["bio"]
            
            user = get_user_model().objects.create_user(email=email, username=email, bio=bio, name=name, 
                                                password = serializer.validated_data["password"])        
            return Response(status=status.HTTP_200_OK)
            
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(errors = serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)


        

