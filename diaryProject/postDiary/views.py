from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment
from django.conf import settings

def home(request): 
    post_list = Post.objects.all().order_by('-id')
    context = {
        'post_list' : post_list
    }
    return render(request, "main.html", context)

def get_count(post):
    comment_list = Comment.objects.filter(post=post)
    comment_count = comment_list.count()
    return comment_count

def mainlist(request) : 
    post_list = Post.objects.all().order_by('-id')
    context = {'post_list': post_list}
    for post in post_list:
        comment_count = get_count(post)
        post.comment_count = comment_count
    return render(request, "mainList.html", context)

@login_required
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
    comment_list = Comment.objects.filter(post=id).order_by('-id')
    comment_count = comment_list.count()
    if request.method == 'POST' :
        content = request.POST.get('content')
        if content :
            post.content = content
            post.save()
        return redirect('post_update', post.id)
    else :
        context = {'post' : post,
        'comment_list' : comment_list,
        'comment_count' : comment_count
        }
        return render(request, 'check.html', context)

@login_required
def post_delete(request, id) :
    post = Post.objects.get(pk=id)
    post.delete()   
    return redirect('home')

def comment_create(request, id) :
    if request.method == 'POST' :
        post = get_object_or_404(Post, pk=id)
        comment = request.POST.get('comment_content')    
        Comment.objects.create (
            comment=comment,
            writer=request.user,
            post=post
        )
    return redirect('post_update', id)

def comment_delete(request, post_id, com_id) :
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('post_update', post_id)