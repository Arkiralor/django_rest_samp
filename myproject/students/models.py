from typing import Optional
from django.db import models

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=16)
    mname = models.CharField(max_length=16, blank=True)
    lname = models.CharField(max_length=16)
    legacy = models.CharField(max_length=4, blank=True)
    roll_no = models.IntegerField()
    standard = models.IntegerField()
    section = models.CharField(max_length=1)
    date_of_birth = models.DateField(default='1992-09-25')

    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname} {self.legacy}"
