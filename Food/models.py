from django.db import models
from Register.models import User,Company


def get_upload_path(instance,image_name):
    return "FoodImage/{0}/{1}".format(instance.id,image_name)
class Food(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank = True)
    name = models.TextField(null=True,blank = True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=get_upload_path, height_field=None, width_field=None, max_length=100,blank = True,null = True)
    amount = models.IntegerField(null=True,blank = True)
    company = models.CharField(max_length=200,null=True,blank=True)
    price = models.DecimalField(null=True,blank=True,max_digits=5,decimal_places=0)
