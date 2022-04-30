from django.contrib import admin

from ToDoList.models import Task
from .models import Task
# Register your models here.
admin.site.register(Task)