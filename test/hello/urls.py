from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    re_path(r'^some-url', views.some_url, name="some_url"),
    path('calc', views.calc, name="calc"),
    path('about', views.about, name="about", kwargs={"name":"Tom", "age": 38})
]