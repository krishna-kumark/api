from django.db import models

# Create your models here.
class Activity(models.Model):
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)

class User(models.Model):
    id_num = models.IntegerField()
    name = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)
    
    

