from django.db import models


from Register.models import User


class Note(models.Model):
    title=models.CharField(max_length=225)
    text=models.TextField()
    
# Create your models here.

class Files(models.Model):
    file=models.FileField(blank=True,null=True)
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
