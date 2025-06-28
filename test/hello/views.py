from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseBadRequest, HttpResponseForbidden

def index(request):
    return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")
    return HttpResponse("Error", status=400, reason="Incorrect data")
    return HttpResponse("Hello World", headers={"SecretCode": "21234567"})

def some_url(request):
    return HttpResponse("Some url")

def calc(request):
    a = int(request.GET.get('a', 10))
    b = int(request.GET.get('b', 20))
    
    result = a + b
    
    return HttpResponse(f"{a} + {b} = {result}")

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
    

def user(request, name="Undefined", age=0):
    return HttpResponse(f"User: {name} <br> Age: {age}")

def products(request, id):
    return HttpResponse(f"Product: {id}")
 
def new(request, id):
    return HttpResponse(f"Comment: {id}")
 
def top(request, id):
    return HttpResponse(f"Question: {id}")

def block(request):
    width = request.GET.get("width", 0)
    height = request.GET.get("height", 0)
    return HttpResponse(f"<h2>Width: {width} Height: {height}</h2>")

def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Incorrect data")
    if (age > 17):
        return HttpResponse("Access accept!")
    else:
        return HttpResponseForbidden("Access denied: age restriction")