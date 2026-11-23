from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Register API
@api_view(['POST'])
def register(request):

    name = request.data.get('name')
    password = request.data.get('password')

    if not name or not password:
        return Response({
            "message": "Name and password are required"
        })

    if User.objects.filter(username=name).exists():
        return Response({
            "message": "Account already exists"
        })

    user = User.objects.create_user(
        username=name,
        password=password
    )

    return Response({
        "message": "Account created successfully",
        "name": user.username
    })


# Login API
@api_view(['POST'])
def login(request):

    name = request.data.get('name')
    password = request.data.get('password')

    user = User.objects.filter(username=name).first()

    if user is None:
        return Response({
            "message": "Invalid username or password"
        })

    if not user.check_password(password):
        return Response({
            "message": "Invalid username or password"
        })

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "name": user.username,
        "token": token.key
    })