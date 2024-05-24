from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование категории',
    )
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='product_store/images/category/',
        null=True,
        default=None,
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование подкатегории',
    )
    slug = models.SlugField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories_of_category'
    )
    image = models.ImageField(
        upload_to='product_store/images/subcategory/',
        null=True,
        default=None,
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование продукта',
    )
    slug = models.SlugField()
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products_subcategory'
    )
    price = models.DecimalField(
        max_digits=19, decimal_places=2
    )
    image_small = models.ImageField(
        upload_to='product_store/images/product/',
        null=True,
        default=None,
        verbose_name='Изображение маленькое',
    )
    image_medium = models.ImageField(
        upload_to='product_store/images/product/',
        null=True,
        default=None,
        verbose_name='Изображение среднее',
    )
    image_large = models.ImageField(
        upload_to='product_store/images/product/',
        null=True,
        default=None,
        verbose_name='Изображение большое',
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class CartedProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='products_carted'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_cart_owner'
    )
    quantity = models.IntegerField(
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return f'{self.product} added to cart by {self.user}'
