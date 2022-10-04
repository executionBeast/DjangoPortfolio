from django.contrib import admin
from blogs.models import Comment
from blogs.models import BlogContent
# Register your models here.
admin.site.register(Comment)
admin.site.register(BlogContent)