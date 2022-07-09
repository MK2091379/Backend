from datetime import date
from django.db import models
from Register.models import User

class TimeAndDateTracker(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank = True)
    created_date = models.DateField(null=True , blank=True)
    start_point = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    end_point = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    #duration=  models.FloatField(null=True,blank = True)
    wasted_time = models.PositiveIntegerField(null=True,blank = True)

    def time_minus(self):

        from datetime import datetime
        calculate_time=str(datetime.combine(date.today(), self.end_point) - datetime.combine(date.today(), self.start_point))
        print(calculate_time)
        return int(calculate_time.split(':')[0])


