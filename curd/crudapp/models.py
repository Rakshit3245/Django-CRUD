from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="student Name")
    email = models.EmailField(max_length=50,verbose_name="student email") 

    def __int__(self):
        return  self.id

