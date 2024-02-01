from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prod_img = models.ManyToManyField('ProductImage', related_name='product_img')
    appuser_id= models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    # product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image {self.id}"