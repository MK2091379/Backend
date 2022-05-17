from django.db import models


from Register.models import User


class Note(models.Model):
    title=models.CharField(max_length=225)
    text=models.TextField()
    file=models.FileField(null=True,blank=True)
# Create your models here.
