from django.db import models
from PIL import Image

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 120)
    price = models.DecimalField(null=True,max_digits=4,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default="default.jpg",  upload_to="food")

    def __str__(self):
        return self.name

    #Resizes photos as they are uploaded
    def save(self, *args, **kwargs):
        super(Food, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)