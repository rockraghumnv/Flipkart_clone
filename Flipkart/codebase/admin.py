from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','image','banner_image')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','logo')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
