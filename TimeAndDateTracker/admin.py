from django.contrib import admin

from TimeAndDateTracker.apps import TimeanddatetrackerConfig
from .models import TimeAndDateTracker
# Register your models here.
admin.site.register(TimeAndDateTracker)