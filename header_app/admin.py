from django.contrib import admin
from .models import tabar
from django.utils.html import format_html
# Register your models here.
class TabarAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'company_name', 'email', 'phone', 'logo_column', 'scrolled_logo_column', 'created_at']
    list_display_links = ['id', 'address', 'email', 'phone', 'company_name']
    search_fields = ['id', 'address', 'email', 'phone']
    list_filter = ['created_at']
    ordering = ['id']
    
    def logo_column(self, obj):
        return self._create_image_column(obj.logo, "Main Logo")
    logo_column.short_description = 'Logo'
    logo_column.admin_order_field = 'logo'
    
    def scrolled_logo_column(self, obj):
        return self._create_image_column(obj.scrolled_logo, "Scrolled Logo")
    scrolled_logo_column.short_description = 'Scrolled Logo'
    scrolled_logo_column.admin_order_field = 'scrolled_logo'
    
    def _create_image_column(self, image_field, title):
        if image_field and hasattr(image_field, 'url'):
            return format_html(
                '<div title="{}" style="cursor: help;">'
                '<img src="{}" style="max-height: 40px; max-width: 40px; '
                'border: 1px solid #ddd; border-radius: 3px; padding: 2px;" />'
                '</div>',
                title,
                image_field.url
            )
        return format_html(
            '<span style="color: #999; font-style: italic;">No {}</span>',
            title.lower()
        )

admin.site.register(tabar, TabarAdmin)