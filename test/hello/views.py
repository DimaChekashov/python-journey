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

def about(request, name, age):
    return HttpResponse(f"""
        <h2>О пользователе</h2>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>                    
    """)
    
def index_request(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)