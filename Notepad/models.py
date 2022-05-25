from django.db import models


from Register.models import User


class Note(models.Model):

    title=models.CharField(max_length=225)
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
# Create your models here.

class Files(models.Model):
    file=models.FileField(blank=True,null=True)
    note=models.ForeignKey(Note,on_delete=models.CASCADE,null=True)
