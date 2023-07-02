from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    titleDate = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    body = models.TextField(verbose_name="내용", default="")
    image = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post-image')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return self.title
    
class Comment(models.Model) :
    comment = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return self.comment