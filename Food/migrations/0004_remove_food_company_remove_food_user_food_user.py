# Generated by Django 4.0.3 on 2022-05-20 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Food', '0003_food_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='company',
        ),
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.AddField(
            model_name='food',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
