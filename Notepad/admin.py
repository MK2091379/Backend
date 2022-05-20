from msilib.schema import File
from django.contrib import admin

from Notepad.models import Note,Files

# Register your models here.
admin.site.register(Note)
admin.site.register(Files)