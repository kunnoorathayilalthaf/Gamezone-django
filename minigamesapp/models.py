from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=250,verbose_name="category_title")
    slug=models.SlugField(max_length=55,verbose_name="category_slug")
    description=models.TextField(blank=True,verbose_name="category_description")
    image=models.ImageField(upload_to="categories",blank=True,null=True,verbose_name="category_image")
    is_active=models.BooleanField(verbose_name="is_active")
    is_featured=models.BooleanField(verbose_name="is_featured")

    def __str__(self):
        return '{}'.format(self.title)
    
    
class Products(models.Model):
    title=models.CharField(max_length=250,verbose_name="products_title")
    slug=models.SlugField(max_length=55,verbose_name="products_slug")
    description=models.TextField(blank=True,verbose_name="product_description")
    image=models.ImageField(upload_to="products",blank=True,null=True,verbose_name="products_image")
    gamelink=models.TextField(blank=True,verbose_name="game_link")
    category=models.ForeignKey(Category,verbose_name="product_category",on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="is_active")
    is_featured=models.BooleanField(verbose_name="is_featured")
    

    def __str__(self):
        return '{}'.format(self.title)

class Cart(models.Model):
    user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
    product=models.ForeignKey(Products,verbose_name='Product',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.user)