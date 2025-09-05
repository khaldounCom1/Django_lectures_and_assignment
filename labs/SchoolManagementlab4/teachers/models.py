# teachers/models.py

from django.db import models

class Teacher(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"