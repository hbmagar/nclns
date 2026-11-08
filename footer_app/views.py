from django.shortcuts import render
from django.views.generic import TemplateView
from footer_app.models import *
# Create your views here.

class footer_header(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_header'] = footer_about.objects.filter(is_active=True)
        return context
    def get_recent_data(self, **kwargs):
        context = super().get_recent_data(**kwargs)
        context['recent_product_image'] = recent_product_menu.objects.filter(is_active=True)