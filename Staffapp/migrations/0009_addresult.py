# Generated by Django 3.2.5 on 2024-09-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0008_all_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('regno', models.CharField(default=False, max_length=100)),
                ('course', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('mark', models.CharField(max_length=100, null=True)),
                ('grade', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
