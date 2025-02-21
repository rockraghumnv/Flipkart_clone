from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='categoty/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    banner_image = models.ImageField(upload_to='banner_images/')
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
