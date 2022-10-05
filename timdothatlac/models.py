from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(("Username"), max_length=50)
    password = models.CharField(("Password"), max_length=50)    

    