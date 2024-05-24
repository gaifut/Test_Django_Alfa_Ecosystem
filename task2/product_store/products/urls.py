from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, CartedProductViewSet

app_name = 'products'

router_v1 = DefaultRouter()
router_v1.register('products', ProductViewSet, basename='products')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('cart', CartedProductViewSet, basename='cart')

urlpatterns = [
    path('', include(router_v1.urls)),
]
