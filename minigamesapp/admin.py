from django.contrib import admin
from .models import Category,Products
# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display=('title','slug','description','image','is_active','is_featured')
    list_editable=('slug','is_active','is_featured')
    list_filter=('is_active','is_featured')
    search_fields=('title','description')
    prepopulated_fields={"slug":("title",)}

admin.site.register(Category,category_admin)




class product_admin(admin.ModelAdmin):
    list_display=('title','slug','description','image','gamelink','is_active','is_featured')
    list_editable=('slug','is_active','is_featured')
    list_filter=('is_active','is_featured')
    search_fields=('title','description')
    prepopulated_fields={"slug":('title',)}
admin.site.register(Products,product_admin)



