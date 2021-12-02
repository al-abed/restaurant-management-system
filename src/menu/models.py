from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 120)
    course_choices = [
        ('AP', 'Appetizer'),
        ('MN', 'Main'),
        ('DT', 'Dessert'),
        ('DR', 'Drink'),
    ]
    course = models.CharField(max_length = 2, choices = course_choices, null = True)
    price = models.DecimalField(null=True,max_digits=4,decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = ResizedImageField(size=[400,400], quality=100, upload_to="food", blank=True, default="default.jpg")

    def __str__(self):
        return self.name
