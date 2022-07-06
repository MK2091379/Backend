from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _





class Company(models.Model):

    company_name=models.CharField(max_length=255,primary_key=True)
    company_biography=models.TextField()
    
    
    def __str__(self) :
        return self.company_name



class User(AbstractUser):
    ROLE_COMPANY_OWNER='C'
    ROLE_EMPLOYEE='E'
    ROLE_CHOICES=[
        (ROLE_COMPANY_OWNER,'Company Owner'),
        (ROLE_EMPLOYEE,'Employee'),
    ]
    
    sexuality_choises = [
        ("M","Male",),
        ("F","Female",),
        ("O","Other",)
    ]
    maritalـstatus_choises = [
        ("M","Maried",),
        ("S","Single",)
    ]
    degreeـofـeducationـchoises = [
        ("D","Diploma",),
        ("B","Bachelor",),
        ("M","Master",),
        ("O","Other")
    ]
    
    
    
    
    #regex for phone iranian phone number 
    valid_number=[RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')]
    
    first_name=models.CharField(_('first name'),max_length=60)
    last_name=models.CharField(_('last name'),max_length=60)
    email=models.EmailField(_('email address'), unique=True)
    role=models.CharField(max_length=1,choices=ROLE_CHOICES)
    username=models.CharField(_('phone number'),max_length=11,validators=valid_number,unique=True)
    company=models.ForeignKey(Company,on_delete=models.PROTECT,null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True)
    personal_id = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')],null=True,blank=True)
    father_full_name = models.CharField(max_length=50,null=True,blank=True)
    mother_full_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    postal_code = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')],null=True)
    sexuality = models.CharField(max_length=1,choices=sexuality_choises,default="M")
    telephone = models.CharField(max_length=11,null=True)
    maritalـstatus = models.CharField(max_length=1,choices=maritalـstatus_choises,default="S")
    degreeـofـeducation = models.CharField(max_length=1,choices=degreeـofـeducationـchoises,default="O")
    check_transportation=models.BooleanField(default=False)
    room = models.ForeignKey('dormitory.Dormitory',on_delete=models.SET_NULL,null=True,related_name='user_room')
    #validators=[RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$')]
  

    

    
    

    
    
    def __str__(self) :
        return self.email+" "+self.first_name+" "+self.last_name
    class Meta :
        ordering=['last_name']
    