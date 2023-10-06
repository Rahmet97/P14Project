import json
import requests

from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q

from .forms import ProductForm
from .models import Product, ShoppingCard, Picture
from .utils import increment_count, decrement_count


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        # products = Product.objects.all()[:3]
        # product_data = []
        # for product in products:
        #     image = Picture.objects.filter(product=product).first()
        #     product.image = image
        #     print(product.image.image.url)
        #     product_data.append(product)
        # self.context.update({'products': product_data})
        protocol = 'https://' if request.is_secure() else 'http://'
        url = protocol + request.META.get('HTTP_HOST') + reverse('product')
        products = requests.get(url)
        self.context.update({'products': products.json()['data']})
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


class ShopView(View):
    template_name = 'shop.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()
        product_data = []
        for product in products:
            image = Picture.objects.filter(product=product).first()
            product.image = image
            print(product.image.image.url)
            product_data.append(product)
        self.context.update({'products': product_data})
        return render(request, self.template_name, self.context)


def about(request):
    return render(request, "about.html")


class AddProductView(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    # fields = ('name', 'price', 'description')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            author = request.user

            product = Product.objects.create(
                name=name,
                price=price,
                description=description,
                author=author
            )
            images = form.files.getlist('image')
            print('images:', images)
            for image in images:
                picture = Picture.objects.create(
                    image=image,
                    product=product
                )
                picture.save()

            return redirect('/add-product')


class DeleteProductView(DeleteView):
    model = Product
    template_name = ''
    success_url = '/'


class HelloAPIView(View):
    def get(self, request):
        return JsonResponse({'success': True, 'message': 'Hello World!'})


class ProductAPIView(View):

    def get(self, request):
        products = Product.objects.all()[:3]
        products_data = []
        for product in products:
            image = Picture.objects.filter(product=product).first()
            product_dict = {
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'author': product.author.id,
                'image': image.image.url
            }
            products_data.append(product_dict)
        return JsonResponse({'data': products_data})
