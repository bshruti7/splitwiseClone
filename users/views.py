from django.http import HttpResponse
from django.shortcuts import render
from .form import UserSignupForm


def index(request):
    response = "Home Page - Users App"
    return render(request, 'users/index.html')


def signup(request):

    form = UserSignupForm

    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)
