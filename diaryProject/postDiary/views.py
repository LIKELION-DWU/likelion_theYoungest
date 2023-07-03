from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post
from django.conf import settings

def home(request): 
    post_list = Post.objects.all().order_by('-id')
    context = {
        'post_list' : post_list
    }
    return render(request, "main.html", context)  # + post_list

def mainlist(request) : 
    post_list = Post.objects.all().order_by('-id')
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
    
def post_update(request, id) :
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST' :
        content = request.POST.get('content')
        if content :
            post.content = content
            post.save()
        return redirect('post_update', post.id)
    else :
        context = {'post' : post}
        return render(request, 'check.html', context)
    
def post_delete(request, id) :
    post = Post.objects.get(pk=id)
    post.delete()   
    return redirect('home')