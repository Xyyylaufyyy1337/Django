from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('writer', views.writer, name='writer'),
    path('about', views.about, name='about'),
]