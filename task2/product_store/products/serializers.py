from rest_framework import serializers

from .models import Category, Product, SubCategory, CartedProduct


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', read_only=True
    )

    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'category',
            'image',
        )


class CategorySerializer(serializers.ModelSerializer):
    subcategories_of_category = SubCategorySerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'image',
            'subcategories_of_category',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SlugRelatedField(
        slug_field='slug', read_only=True
    )

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'image_small',
            'image_medium',
            'image_large',
        )

    def get_category(self, obj):
        return obj.subcategory.category.name


class CartedProductSerializer(serializers.ModelSerializer):
    product_price = serializers.ReadOnlyField(source='product.price')
    product_total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartedProduct
        fields = (
            'id',
            'product',
            'quantity',
            'product_price',
            'product_total_price',
        )

    def get_product_total_price(self, obj):
        return obj.product.price * obj.quantity
