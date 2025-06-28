from django.urls import path, re_path, include
from . import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]

urlpatterns = [
    path('', views.index, name="home"),
    re_path(r'^some-url', views.some_url, name="some_url"),
    path('calc', views.calc, name="calc"),
    path('about', views.about, name="about", kwargs={"name":"Tom", "age": 38}),
    path('index-request', views.index_request, name="index_request"),
    path('user/', views.user),
    path('user/<name>', views.user),
    path('user/<name>/<int:age>', views.user),
    path("products/<int:id>/", include(product_patterns)),
    path("block", views.block),
    path("contact/", views.contact),
    path("details/", views.details),
    path("access/<int:age>", views.access),
]