from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

## views


def index(request):
    return HttpResponse('hello world.....')

def login(request):
    return HttpResponse('this is login page')
