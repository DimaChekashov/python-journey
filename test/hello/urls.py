from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('some-url', views.some_url, name="some_url"),
    path('calc', views.calc, name="calc"),
]