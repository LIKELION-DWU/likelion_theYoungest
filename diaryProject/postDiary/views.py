from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post
from django.conf import settings

def home(request): 
    post_list = Post.objects.all().order_by('-titleDate')
    context = {
        'post_list' : post_list
    }
    return render(request, "main.html", context)  # + post_list

def mainlist(request) : 
    post_list = Post.objects.all().order_by('-titleDate')
    context = {
        'post_list' : post_list
    }
    return render(request, "mainList.html", context) # + post_list

def create(request) :
    if request.method == 'POST' or request.method == 'FILES' :
        try:
            image = request.FILES.get('image')
        except:
            image = None
        content = request.POST.get('content')
        Post.objects.create (
            image=image,
            content=content,
            writer=request.user
        )

        return redirect('home')
    else :
        return render(request, 'input.html')