from django.urls import path
from .views import create_post, post_list, post_details, delete_post, update_post, user_specific_post_list
urlpatterns = [
    path("create-post/", create_post),
    path("", post_list),
    path("update-post/<int:id>/", update_post),
    path("post-details/<int:id>/", post_details),
    path("delete_post/<int:id>/", delete_post),
    path("user-specific-post-list/<str:username>/", user_specific_post_list),
]
