from django.db import models

# Create your models here.

class userPref(models.Model):
    username = models.CharField(max_length=100)
    pref = models.CharField(max_length=500)

class userRec(models.Model):
    username: str
    url: str
    recipe: str
    cal: str