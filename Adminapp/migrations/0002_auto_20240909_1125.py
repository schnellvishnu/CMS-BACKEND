# Generated by Django 3.2.5 on 2024-09-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmodel',
            name='staff_pwd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='staff_uname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
