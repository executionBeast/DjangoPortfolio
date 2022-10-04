 # return HttpResponse("<h1> First Blog app Successful </h1> <a href='/'>homepage</a>")
 # return HttpResponse("<h1> Second Blog app Successful </h1>  <a href='/'>homepage</a>")


from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Comment
from blogs.models import BlogContent

def blog1(request):
    context={
        'blogcontent':BlogContent.objects.all(),
        'commentdata':Comment.objects.all(),
    }
    if request.method == 'POST':
        name=request.POST.get('name')
        commentdata=request.POST.get('comment')
        if len(name)>=2 and len(commentdata) >=2:
            comment=Comment(name=name,commentdata=commentdata)
            comment.save()
            
    return render(request,'blog1.html',context)



def createblog(request):
    if request.method=='POST':
        name=request.POST.get('name')
        title=request.POST.get('title')
        blogcontent=request.POST.get('blogcontent')

        if len(name)>=1 and len(title)>=1 and len(blogcontent)>=1:
            Blogcontent = BlogContent(name=name,title=title,blogcontent=blogcontent)
            Blogcontent.save()

    return render(request,'createblog.html')




def blog3(request):
    if BlogContent.objects.all():
        context={
            "title":BlogContent.objects.all()[0].title,
            "content":BlogContent.objects.all()[0].blogcontent,
        }
    return render(request,'renderblog.html',context)   #dynamic blog


# Create your views here.
