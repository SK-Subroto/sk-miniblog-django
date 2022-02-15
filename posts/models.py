from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
