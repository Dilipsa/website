from django.db import models
from django.utils import timezone
from users.models import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField()
  created = models.DateTimeField(default=timezone.now)
  is_public = models.BooleanField(default=False)