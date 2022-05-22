from django.db import models
from Register.models import User
# Create your models here.
class EmployeeSalary(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary_hours=models.DecimalField(max_digits=9,decimal_places=0)
    price_food=models.DecimalField(max_digits=9,decimal_places=0)
    price_transportatio=models.DecimalField(max_digits=9,decimal_places=0)
    price_dormitory=models.DecimalField(max_digits=9,decimal_places=0)
    