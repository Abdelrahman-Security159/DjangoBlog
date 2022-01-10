from . import views 
from django.urls import path

urlpatterns  = [
    path('', views.index, name="index"),
    path('posts/<int:id>', views.posts, name="posts"),
    path('explore', views.explore, name="explore"),
    path('path/<str:slug>', views.single_post),
]