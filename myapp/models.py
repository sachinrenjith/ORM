from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique= False)
    email = models.EmailField(max_length=30, unique=False)

    def __str__(self):
        return self.first_name