# Generated by Django 5.1 on 2024-08-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_animal_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
