# Generated by Django 4.0.3 on 2022-05-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transportation', '0004_alter_admintransportation_maximum_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintransportation',
            name='Return_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='admintransportation',
            name='arrival_time',
            field=models.TimeField(null=True),
        ),
    ]
