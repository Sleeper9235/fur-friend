# Generated by Django 5.1 on 2024-08-25 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_animalshelter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalshelter',
            name='animal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.animal'),
        ),
    ]
