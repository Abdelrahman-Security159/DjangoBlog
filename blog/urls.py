from . import views 
from django.urls import path

urlpatterns  = [
    path('', views.index, name="index"),
    path('posts', views.posts),
    path('explore', views.explore, name="explore"),
    path('path/<str:slug>', views.single_post)
]