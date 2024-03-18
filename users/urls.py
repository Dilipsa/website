from django.urls import path
from .views import register_user, login_user, user_profile, update_profile

urlpatterns = [
    path("register-user/", register_user),
    path("login-user/", login_user),
    path("user-profile/", user_profile),
    path("update-profile/", update_profile),
]