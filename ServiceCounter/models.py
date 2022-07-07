from django.db import models
from Register.models import User

# Create your models here.


class RequestForm(models.Model):
    
    pending_mode='P'
    declined_mode='D'
    accepted_mode='A'
    
    status_choice=[
        ('pending','Pending'),
        ('declined','Declined'),
        ('accepted','Accepted'),
    ]

    
    title_form=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,choices=status_choice,default=pending_mode)
    type_form=models.CharField(max_length=150)
    value_form=models.TextField()
    created_time=models.DateField(auto_now_add=True)
    
  
