from unicodedata import name
from django.urls import path
from django.contrib import admin
from users import views as user_views
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserListView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name="blog-about"),
    path('admin/',admin.site.urls),
    path('register/',user_views.register, name='register'),
]