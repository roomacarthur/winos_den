from django.contrib import admin

# Register your models here.
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)