'''
***IMPORTANT path('blogs',views.blog,name='blog'),    
    path('blogs1',views.blog1,name='blog1'),
aise urls daalo aur views me aise handle karo 
def blog(request):
    return HttpResponse("<h1> First Blog app Successful </h1>")

def blog1(request):
    return HttpResponse("<h1> Second Blog app Successful </h1>")

'''

from django.urls import path
# from home import views //pahle maine yeh kiya thaa //par yeh line bol rha hai ke home mein se views ko lekar aao
#aur path me diya hai ki uss views se blogs nikal rha to home ke views me blog hai nhi to no module found hii aayega n
from blogs import views

urlpatterns = [
    path('blog1',views.blog1,name='blog'),    
    # path('blog2',views.blog2,name='blog2'),
    path('createblog',views.createblog,name='createblog'),
    path('blog3',views.blog3,name='blog3'),  #rendered blog
    # path('blog2',views.blog2,name='blog1'),  abhi 2nd blog banaya nhi h
]
