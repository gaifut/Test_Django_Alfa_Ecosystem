from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .models import Category, Product, CartedProduct
from .serializers import (
    CategorySerializer, ProductSerializer, CartedProductSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartedProductViewSet(viewsets.ModelViewSet):
    serializer_class = CartedProductSerializer

    def get_queryset(self):
        return CartedProduct.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        cart_items = CartedProduct.objects.filter(user=request.user)
        total_price = sum(
            item.product.price * item.quantity for item in cart_items
        )
        data = {
            'items': CartedProductSerializer(cart_items, many=True).data,
            'total_price': total_price,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='clear')
    def clear_cart(self, request):
        CartedProduct.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
