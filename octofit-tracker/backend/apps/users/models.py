from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Additional fields can be added here
        groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
        user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_permissions_set')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username