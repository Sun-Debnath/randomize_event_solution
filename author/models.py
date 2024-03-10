from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, related_name = 'author',on_delete=models.CASCADE)
    organizer_or_not = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name