from django.shortcuts import render

def create_post(request):
  return render(request, "blog/create_post.html")

def post_list(request):
  return render(request, "blog/post_list.html")

def post_details(request, id):
  return render(request, "blog/post_details.html")

def update_post(request, id):
  return render(request, "blog/update_post.html")

def delete_post(request, id):
  pass

def user_specific_post_list(request, username):
  return render(request, "blog/user_specific_post_list.html")