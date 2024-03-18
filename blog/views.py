from .models import Post
from django.shortcuts import render, redirect
from django.contrib import messages

def create_post(request):
  if not request.user.is_authenticated:
    return redirect("/users/login-user/")
  if request.method == "POST":
    title = request.POST.get('title')
    content = request.POST.get('content')
    Post.objects.create(title=title, content=content, user=request.user)
    messages.success(request, f"Hi {request.user}, your Post created successfully")
  return render(request, "blog/create_post.html")

def post_list(request):
  posts = Post.objects.all()
  
  context = {
    'posts':posts,
    }
  return render(request, "blog/post_list.html", context)

def post_details(request, id):
  return render(request, "blog/post_details.html")

def update_post(request, id):
  return render(request, "blog/update_post.html")

def delete_post(request, id):
  pass

def user_specific_post_list(request, username):
  return render(request, "blog/user_specific_post_list.html")