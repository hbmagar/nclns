# Create your views here.
from django.shortcuts import render, get_object_or_404

"""include all models here"""
from home_app.models import *  

def home_page(request):
    slides = index_slide.objects.all()
    businesses = our_business.objects.all()
    motives = busisness_motive_list.objects.all()
    new_products = latest_product.objects.all()
    news_portals = news_portal.objects.all()
    event_parts = event_part.objects.all()
    experience_parts = experience_part.objects.all()
    feed_backs = feed_back.objects.all()
    
    context = {
        'slide_show':slides,
        'businesses':businesses,
        'motives':motives,
        'products':new_products,
        'news':news_portals,
        'event_parts':event_parts,
        'experience_parts':experience_parts,
        'feed_backs':feed_backs,
    }
    return render(request, 'webpages/home.html', context)

def index_page(request):
    pass

def about_team(request):
    return render(request, 'home_app/about_team.html')



