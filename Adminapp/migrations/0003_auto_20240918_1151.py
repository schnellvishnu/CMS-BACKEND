# Generated by Django 3.2.5 on 2024-09-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_auto_20240909_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='grade',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='student_pwd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='student_uname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
