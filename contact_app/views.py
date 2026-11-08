from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required   
from .models import Contact_item, contact_map

# Create your views here.

def contact_view(request):
    contact_info = Contact_item.objects.all()
    contact_maping = contact_map.objects.all()
    
    context = {'contact_info': contact_info, 
               'contact_map': contact_maping
               }
    return render(request, 'webpages/contact.html', context)
