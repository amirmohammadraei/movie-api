from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.contrib.auth.hashers import make_password



ROLE_CHOICES =(
    (1, "User"),
    (2, "Admin"),
)
class User(AbstractUser):
    role = models.IntegerField(choices=ROLE_CHOICES, null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super(User, self).save(*args, **kwargs)


class Movie(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    movie_id = models.IntegerField()

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    approved = models.BooleanField(null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now())
    movie_id = models.IntegerField()

    def __str__(self):
        return self.user.username
