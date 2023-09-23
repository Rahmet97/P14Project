from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import HomeView, shop, about, ShoppingCartView, IncrementCountView, DecrementCountView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement'),
]
