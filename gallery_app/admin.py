from django.contrib import admin
from .models import Gallery_Item
from django.utils.html import format_html

# Register your models here.
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_title', 'image_descriptions', 'gallery_img', 'created_at')
    list_display_links = ('id', 'gallery_title', 'image_descriptions', 'gallery_img')
    search_fields = ('gallery_title',)
    def gallery_img(self, obj):
        if obj.gallery_image and obj.gallery_image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.gallery_image.url
            )
        return "─"
    readonly_fields = ('created_at',)
    ordering = ('id',)
admin.site.register(Gallery_Item, GalleryItemAdmin)