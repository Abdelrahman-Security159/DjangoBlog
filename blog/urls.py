from . import views 
from django.urls import path

urlpatterns  = [
    path('', views.index),
    path('posts', views.posts),
    path('path/<str:slug>', views.single_post)
]