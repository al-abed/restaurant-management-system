from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 120)
    type_choices = [
        ('AP', 'Appetizer'),
        ('MN', 'Main'),
        ('DT', 'Dessert'),
    ]
    type = models.CharField(max_length = 2, choices = type_choices, null = True)
    price = models.DecimalField(null=True,max_digits=4,decimal_places=2)
    description = models.TextField(null=True, blank=True)

    image = ResizedImageField(size=[400,400], quality=100, upload_to="food")

    def __str__(self):
        return self.name
