from django.db import models
# Create your models here.


class Dormitory(models.Model):
    number = models.IntegerField(null = True,blank=True)
    capacity = models.IntegerField(null = True,blank = True)
    user = models.ForeignKey(null = True,blank = True)
    company = models.CharField(max_length=200,null=True,blank=True)
