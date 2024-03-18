from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   # Custom user model, inherited from builtin User model
  profile_pic = models.ImageField(upload_to="profile_pictures")




