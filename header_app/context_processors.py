from .models import tabar

def tab_items_processor(request):
    tab_items = tabar.objects.all()
    return {'tab_items': tab_items}
