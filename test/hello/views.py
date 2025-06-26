from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def some_url(request):
    return HttpResponse("Some url")

def calc(request):
    a = 10
    b = 20
    return HttpResponse(f"{a} + {b} = {a + b}")