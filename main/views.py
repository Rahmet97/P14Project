from django.shortcuts import render, HttpResponse

from .models import Product


def home(request):
    products = Product.objects.all()[:3]
    return render(request, "index.html", {'products': products})


def shop(request):
    return render(request, "shop.html")


def about(request):
    return render(request, "about.html")
