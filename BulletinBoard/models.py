from operator import truediv
from django.db import models

# Create your models here.
class BulletinBoard(models.Model):
    html_fields = models.TextField(null=True,blank = True)
    title = models.CharField(max_length=200,null=True,blank=True)