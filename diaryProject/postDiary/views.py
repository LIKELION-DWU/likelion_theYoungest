from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post
from django.conf import settings

def home(request): 
    post_list = Post.objects.all().order_by('-id')
    context = {
        'post_list' : post_list
    }
    return render(request, "main.html", context)

def mainlist(request) : 
    post_list = Post.objects.all().order_by('-id')
    context = {
        'post_list' : post_list
    }
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

# 댓글 read 부분은 여기에 구현 해주세용 
# 댓글 가져오기(R) : comment = Comment.objects.filter(post=pk).order_by('-id')
# 댓글 수 가져오는 거 : comment_count = comment.exclude(deleted=True).count()
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

@login_required
def post_delete(request, id) :
    post = Post.objects.get(pk=id)
    post.delete()   
    return redirect('home')

# 댓글 생성(C) + 삭제 (D)구현 필요 (수정(U)까지는 안해도 될 것 같아요 + 하면 좋고!)
# 사용자가 작성한 댓글 내용은 comment = request.POST.get('comment_content') 으로 받아옵니다 
# writer = request.user로 따로 저장해주세요 ! 
def comment_create(request, id) :
    pass

# 삭제는 id가 두 개 ! 
def comment_delete(request, post_id, msg_id) :
    pass