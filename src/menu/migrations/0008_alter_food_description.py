# Generated by Django 3.2.9 on 2021-11-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(null=True),
        ),
    ]