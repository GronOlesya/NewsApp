from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render


class PostsList(ListView):
    model = Post
    ordering = '-post_create_time'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# Create your views here.
