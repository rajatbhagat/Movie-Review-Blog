from django.shortcuts import render
from django.http import HttpResponse
from movieBlog.models import Post, Comments, UserAttributes
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return HttpResponse("Yes this works")


def get_all_posts(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'movieBlog/post_list.html', context_dict)
