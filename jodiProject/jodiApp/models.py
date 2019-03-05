from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserLoginModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    dateAccountCreated = models.DateField(default="")
    rank = models.CharField(max_length=200, default="grunt")
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class GameModel(models.Model):
    name = models.CharField(max_length=20)
    developer = models.CharField(max_length=20)
    dateMade = models.DateField(default="")
    ageLimit = models.IntegerField()
    gameForeignkey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
