from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import random


all_idx = ['', '', '']

def get_random_idx():
    posts = Post.objects.all()
    posts_count = posts.count()
    counter = 0
    while True:
        if counter != 3:
            random_number = random.randrange(0, posts_count)
            if random_number not in all_idx:
                all_idx[counter] = random_number
                counter += 1
        else:
            break

def index(request):
    get_random_idx()
    posts = Post.objects.all()
    
    first = posts[all_idx[0]]
    second = posts[all_idx[1]]
    third = posts[all_idx[2]]
    
    return render(request, "index.html", {
        "first" : first,
        "second" : second,
        "third" : third
    })

def posts(request, id):
    return render(request, "post.html", {
        "post" : Post.objects.get(pk=id)
    })

def explore(request):
    all_posts = Post.objects.all()
    num_posts = all_posts.count()
    
    return render(request, "explore.html", {
        "posts" : all_posts,
        "count" : num_posts
    })

def single_post(request):
    pass
    