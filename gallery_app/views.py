from django.shortcuts import render
from .models import Gallery_Item

# Create your views here.
def gallery_items(request):
    gallery_data = Gallery_Item.objects.all()
    context = {'gallery_data': gallery_data}
    return render(request, 'webpages/gallery.html', context)