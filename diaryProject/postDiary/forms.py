from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
            # 어떤 필드를 입력 받을지 써주기
        fields = ['content', 'image'] 

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['comment']