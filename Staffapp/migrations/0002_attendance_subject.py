# Generated by Django 3.2.5 on 2024-09-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
