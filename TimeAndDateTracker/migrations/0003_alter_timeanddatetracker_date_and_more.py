# Generated by Django 4.0.3 on 2022-04-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeAndDateTracker', '0002_rename_difference_timeanddatetracker_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeanddatetracker',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeanddatetracker',
            name='delay',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeanddatetracker',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeanddatetracker',
            name='end_point',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeanddatetracker',
            name='start_point',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
