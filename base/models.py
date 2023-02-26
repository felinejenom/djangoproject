from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=300)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Topics(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    class Meta:
        ordering = [
            '-updated',
            '-created'
        ]

