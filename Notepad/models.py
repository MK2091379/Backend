from django.db import models


from Register.models import User


class Note(models.Model):

    title=models.CharField(max_length=225, null=False)
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
# Create your models here.

def get_upload_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.note.id, filename)
class Files(models.Model):
    file=models.FileField(upload_to=get_upload_path,blank=True,null=True)
    note=models.ForeignKey(Note,on_delete=models.CASCADE,null=True)
