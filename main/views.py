import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Product, ShoppingCard
from .utils import increment_count, decrement_count


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()[:3]
        self.context.update({'products': products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user_id = request.user.id
        shopping_card = ShoppingCard.objects.create(
            product_id=id,
            user_id=user_id
        )
        shopping_card.save()
        messages.info(request, 'Added successfully!')
        return redirect('/')


class ShoppingCartView(View):
    template_name = 'cart.html'
    context = {}

    def get(self, request):
        shopping_cart = ShoppingCard.objects.filter(user=request.user).values('product_id')
        products = Product.objects.filter(pk__in=shopping_cart)
        data = []
        for product in products:
            shop = ShoppingCard.objects.get(Q(user=request.user) & Q(product=product))
            product.count = shop.count
            data.append(product)
        self.context.update({'products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        shopping_cart = ShoppingCard.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.delete()
        return redirect('/cart')


class IncrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id=None
        result = increment_count(id, request.user)
        return JsonResponse({'result': result})


class DecrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = decrement_count(id, request.user)
        return JsonResponse({'result': result})


def shop(request):
    return render(request, "shop.html")


def about(request):
    return render(request, "about.html")
