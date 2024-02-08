from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={'unique':'이미 있는 제목입니다.'})
    content = models.TextField()
    nicknames = models.CharField(max_length=50)
    dt_created = models.DateTimeField(verbose_name="Date Create", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    
    def __str__(self):
        return self.title