from django.contrib import admin

from .models import Category, SubCategory, Product


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, ProductAdmin)
admin.site.register(SubCategory, ProductAdmin)
