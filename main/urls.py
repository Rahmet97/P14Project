from django.urls import path

from .views import home, shop, about

urlpatterns = [
    path('', home, name='home'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),
]
