from django.shortcuts import render


def register_user(request):
  return render(request, 'users/register_user.html')

def login_user(request):
  return render(request, 'users/login_user.html')

def user_profile(request):
  return render(request, 'users/user_profile.html')

def update_profile(request):
  return render(request, 'users/update_profile.html')