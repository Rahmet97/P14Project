from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import HomeView, ShopView, about, ShoppingCartView, IncrementCountView, DecrementCountView, AddProductView, \
    HelloAPIView, ProductAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('about', about, name='about'),
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement'),
    path('add-product', AddProductView.as_view(), name='add_product'),
    path('hello', HelloAPIView.as_view(), name='hello'),
    path('products', ProductAPIView.as_view(), name='product'),
]
