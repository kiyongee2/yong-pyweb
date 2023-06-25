from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    #ordering = ['-created']

admin.site.register(Category, CategoryAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'price', 'stock',
                    'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'available_order', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']
    #ordering = ['-created']
