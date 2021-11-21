from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 120)
    price = models.DecimalField(default=0,max_digits=4,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name