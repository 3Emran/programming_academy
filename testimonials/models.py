from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name
