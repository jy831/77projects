from django.urls import path
from . import views

app_name = 'pickever'

urlpatterns = [
    path('', views.index, name='index'),
    path('music/create/', views.music_create, name='music_create'),
]