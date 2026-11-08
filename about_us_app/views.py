# Create your views here.
from django.shortcuts import render, get_object_or_404

"""include all models here"""
from about_us_app.models import * 

def about_us(request):
    about_us_contents = AboutUs.objects.all()
    about_aims_contents = about_aims.objects.all()
    about_partners_header_contents = about_partners_header.objects.all()
    partners_logo_contents = partners_logo.objects.all()
    context = {
        'about_us_contents': about_us_contents,
        'about_aims_contents': about_aims_contents,
        'about_partners_header_contents': about_partners_header_contents,
        'partners_logo_contents': partners_logo_contents,
    }
    return render(request, 'webpages/about_us.html', context)