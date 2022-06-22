from django.db import models
from Register.models import User
# Create your models here.
class EmployeeSalary(models.Model):
    employee=models.OneToOneField(User,on_delete=models.CASCADE)
    monthly_salary=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    reward_benefit=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    min_working=models.PositiveIntegerField()
         

    
    
    
    