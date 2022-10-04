from django.db import models

# Create your models here.

class Comment(models.Model):
    name=models.CharField('name',max_length=50)
    commentdata=models.TextField('comment',max_length=200)
    def __str__(self):
        return self.name



class BlogContent(models.Model):
    name=models.CharField('name',max_length=50)
    title= models.CharField('title',max_length=200)
    blogcontent=models.TextField('BlogContent',max_length=500)

    def __str__(self):
        return self.name

