from django.shortcuts import render
from product_app.models import *

# Create your views here.
def product_details(request):
    products_about = about_product.objects.all()
    prodduct_items = product_list.objects.all()
    upcoming_products = upcoming_product.objects.all()
    deals_product_item = deals_product.objects.first()
    context = {
        'products_about': products_about,
        'prodduct_items': prodduct_items,
        'upcoming_products': upcoming_products,
        'deals_product_item': deals_product_item,
    }
    return render(request, 'webpages/product.html', context)
