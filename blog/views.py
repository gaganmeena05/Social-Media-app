from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augest 27,2022'
    },
    {
        'author': 'Jon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Augest 28,2022'
    }
]

def home(request):
    context={
        'posts':posts,
    }
    return render(request,'./blog/home.html',context)

def about(request):
    return render(request,'./blog/about.html',{'title': 'ABOUT'})
