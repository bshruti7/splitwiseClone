from django.http import HttpResponse
from django.shortcuts import render
from .form import UserSignupForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreateUserSerializer, UserSerializer
from django.contrib.auth.models import User


def index(request):
    response = "Home Page - Users App"
    all_users = User.objects.all()
    print(all_users)
    return render(request, 'users/index.html')


def signup(request):

    form = UserSignupForm

    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)


@api_view(['POST'])
def create_user(request):

    serializer = CreateUserSerializer(data=request.data)
    response_data = {
        'errors': None,
        'data': None
    }
    if serializer.is_valid():
        serializer.save()
        response_data['data'] = serializer.data
        return Response(response_data, status=status.HTTP_201_CREATED)
    else:
        response_data['errors'] = serializer.errors
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
