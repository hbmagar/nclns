from django.shortcuts import render
from django.views.generic import TemplateView
from header_app.models import tabar
# Create your views here.

class Tabmenu(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tab_items'] = tabar.objects.filter(is_active=True)
        return context