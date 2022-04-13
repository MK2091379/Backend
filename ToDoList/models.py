
from django.db import models
from Register.models import User 

# Create your models here.

class Task(models.Model):

    description=models.TextField()
    checkbox=models.BooleanField(default=False)
    deadline=models.DateTimeField()
    last_update=models.DateTimeField( auto_now=True)
    creation_time=models.DateTimeField( auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    