from django.db import models
from django.forms import DateField
from Register.models import User


class Report(models.Model):
    
    type_report_choices=[
        ('expense','Expense'),
        ('income','Income'),
   
                        ]
    period_choices=[
           ('daily','Daily'),
           ('weekly','Weekly'),
           ('monthly','monthly'),
           ('annual','Annual'),
           ('onetime','One Time'),
          
     ]
    
    
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    type_report=models.CharField(max_length=7,choices=type_report_choices,default='expense')
    amount=models.DecimalField(max_digits=6,decimal_places=2)
    period=models.CharField(max_length=9,choices=period_choices,default='daily')
    created_time=models.DateField(auto_now_add=True)
    date_period=models.DateField()
    
    
    
# Create your models here.