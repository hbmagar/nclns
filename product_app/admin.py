from django.contrib import admin
from product_app.models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.
class service_element(admin.ModelAdmin):
    list_display = ('id', 'product_about_header','product_focus_header','explain', 'image_gallery', 'btn_text')
    list_display_links = ('id', 'product_about_header','product_focus_header','explain', 'image_gallery', 'btn_text')
    
    # Show all images in one cell
    def image_gallery(self, obj):
        images = []
        for i in range(1, 5):
            img_field = getattr(obj, f'img{i}', None)
            if img_field:
                images.append(f'<img src="{img_field.url}" height="50" style="margin: 2px;">')
        
        if images:
            return mark_safe(" ".join(images))
        return "No Images"
    
    image_gallery.short_description = 'Images'
admin.site.register(about_product, service_element)
class product_element(admin.ModelAdmin):
    list_display = ('id', 'product_header', 'image_preview', 'place','star_rate','published_date')
    list_display_links = ('id', 'product_header', 'image_preview', 'place', 'star_rate', 'published_date')
    list_filter = ('published_date', 'price', 'place')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Image'
    ordering = ['id']
admin.site.register(product_list, product_element)

class upcoming_product_element(admin.ModelAdmin):
    list_display = ('id', 'product_header', 'image_preview', 'product_about','published_date', 'product_status', 'react_rate','username')
    list_display_links = ('id', 'product_header', 'image_preview', 'product_about', 'published_date', 'product_status', 'react_rate', 'username')
    list_filter = ('published_date', 'product_status')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image'
    ordering = ['id']
admin.site.register(upcoming_product, upcoming_product_element)

class deals_product_element(admin.ModelAdmin):
    list_display = ('id', 'deal_title', 'image_preview', 'deal_header','deal_description','deal_slogan','whatsapp_link','facebook_link','google_link')
    list_display_links = ('id', 'deal_title', 'image_preview', 'deal_header', 'deal_description','deal_slogan', 'whatsapp_link', 'facebook_link', 'google_link')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Image'
    ordering = ['id']
admin.site.register(deals_product, deals_product_element)