from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('hello world.....')

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def table(request):
    return render(request, 'tables.html')