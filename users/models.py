from django.db import models
from django.contrib.auth.models import User

#
# class TimeStamp(models.Model):
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     readonly_fields =
#
#     class Meta:
#         abstract = True
#


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_verified = models.BooleanField(default=False)




