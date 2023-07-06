from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    titleDate = models.DateField(verbose_name="작성일", auto_now_add=True)
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post-image')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return str(self.titleDate)
    
class Comment(models.Model) :
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.comment