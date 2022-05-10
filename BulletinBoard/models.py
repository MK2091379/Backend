from django.db import models

# Create your models here.
class BulletinBoard(models.Model):
    html_fields = models.TextField(null=True,blank = True)