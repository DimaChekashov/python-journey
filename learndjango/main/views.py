from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h4>Check working...</h4>")

def about(request):
    return HttpResponse("<h4>About page</h4>")

def profile(request):
    return HttpResponse("<h4>Profile page</h4>")