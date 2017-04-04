from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user        = models.OneToOneField(User)

    # will work out on streak in the second version.
    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['user']
