# Generated by Django 4.0.3 on 2022-05-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notepad', '0004_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
