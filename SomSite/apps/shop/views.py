from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


def shop_view(request):
    if request.method == 'GET':
        context = {
            'product': Product.objects.all()
        }
        return render(request, 'shop/shop.html', context)
    pass


