from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=20)
    university = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    