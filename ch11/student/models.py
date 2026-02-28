from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.TextField(max_length=250)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    city=models.TextField(max_length=250, default='xyz')