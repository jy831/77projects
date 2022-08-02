from django.urls import path
from . import views

app_name = 'pickever'

urlpatterns = [
    path('', views.index, name='index'),
    path('music/create/', views.music_create, name='music_create'),
    path('music/delete/<int:music_id>/', views.music_delete, name='music_delete'),
path('music/vote/<int:music_id>/', views.music_vote, name='music_vote'),
    path('report/create/', views.report_create, name='report_create'),
]