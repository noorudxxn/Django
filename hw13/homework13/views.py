from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import NoteSerializer


# Signup API
@api_view(['POST'])
def signup(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({
            "message": "Username already exists"
        })

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response({
        "message": "User registered successfully"
    })


# Login API
@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user:

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "username": user.username,
            "token": token.key
        })

    return Response({
        "message": "Invalid username or password"
    })


# Add and List Notes
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def notes(request):

    # List notes
    if request.method == 'GET':

        notes = Note.objects.filter(user=request.user)

        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)

    # Add note
    elif request.method == 'POST':

        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response({
                "message": "Note added successfully",
                "note": serializer.data
            })

        return Response(serializer.errors)