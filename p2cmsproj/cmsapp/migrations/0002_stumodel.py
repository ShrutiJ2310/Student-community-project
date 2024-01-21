# Generated by Django 5.0 on 2023-12-18 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuModel',
            fields=[
                ('rno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.deptmodel')),
            ],
        ),
    ]
