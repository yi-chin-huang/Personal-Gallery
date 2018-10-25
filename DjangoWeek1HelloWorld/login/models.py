from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.

class User(models.Model):
	username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	password = models.CharField(max_length=20)
	objects =  UserManager()
	def __str__(self):
		return self.username + " " + self.password
