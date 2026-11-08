from django.contrib import admin
from footer_app.models import *
from django.utils.html import format_html

class footer_abouts(admin.ModelAdmin):
    list_display = ['id', 'full_company_name', 'company_slogan', 'company_about', 'copyright_date', 'copyright_name']
    list_display_links = ['id', 'full_company_name', 'company_slogan', 'company_about', 'copyright_date', 'copyright_name']
    search_fields = ['id', 'copyright_date']
    list_filter = ['copyright_date']
    ordering = ['id']
admin.site.register(footer_about, footer_abouts)

class footer_recent_pro(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'slide_items', ]
    list_display_links = ['id', 'product_name', 'slide_items']
    search_fields = ['id', 'product_name']
    list_filter = ['product_name']
    def slide_items(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ['id']

admin.site.register(recent_product_menu, footer_recent_pro)