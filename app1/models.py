from django.db import models

# Create your models here



class dept(models.Model):
    facultyname = models.CharField(max_length=30)
    doj = models.DateField()

class deptname(dept):
    it = models.BooleanField(max_length=30, default=False)
    electrical = models.BooleanField(max_length=30, default=False)
    mechanical = models.BooleanField(max_length=30, default=False)
