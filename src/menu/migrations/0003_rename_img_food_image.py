# Generated by Django 3.2.9 on 2021-11-22 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_food_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='img',
            new_name='image',
        ),
    ]