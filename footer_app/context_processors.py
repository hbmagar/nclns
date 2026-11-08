from .models import footer_about, recent_product_menu

def footer_content_processor(request):
    footer_ab = footer_about.objects.all()
    footer_product = recent_product_menu.objects.all()
    return {'footer_header': footer_ab,'recent_product_image': footer_product
            
            }
