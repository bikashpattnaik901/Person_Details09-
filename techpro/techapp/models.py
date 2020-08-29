from django.db import models

# Create your models here.

class Employee(models.Model):
    person = models.CharField(max_length=20)
    groupp = models.IntegerField()
    age = models.IntegerField()
    
  