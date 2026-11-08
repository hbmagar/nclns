from django.contrib import admin
from django.utils.html import format_html

"""include all models here"""
from about_us_app.models import *  


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_title', 'about_header', 'about_us', 'first_btn', 'second_btn', 'image_tag')
    list_display_links = ('id', 'about_title', 'about_header', 'about_us', 'first_btn', 'second_btn', 'image_tag')
    search_fields = ('about_title', 'about_header', 'about_us', 'first_btn', 'second_btn', 'image_tag')
    list_filter = ('about_title',)
    def image_tag(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ('-id',)
admin.site.register(AboutUs, AboutUsAdmin)

class about_aimsAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_aim_title', 'about_aim', 'about_aim_icon')
    list_display_links = ('id', 'about_aim_title', 'about_aim', 'about_aim_icon')
    search_fields = ('about_aim_title', 'about_aim', 'about_aim_icon')
    list_filter = ('about_aim_title',)
    ordering = ('-id',)
admin.site.register(about_aims, about_aimsAdmin)

class about_partners_headerAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner_header','partner_title', 'trust_type', 'trust_icon')
    list_display_links = ('id', 'partner_header','partner_title', 'trust_type', 'trust_icon')
    search_fields = ('partner_header',)
    list_filter = ('partner_header',)
    ordering = ('-id',)
admin.site.register(about_partners_header, about_partners_headerAdmin)

class partners_logoAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner_logo', 'image_tag')
    list_display_links = ('id', 'partner_logo', 'image_tag')
    search_fields = ('partner_logo',)
    list_filter = ('partner_logo',)
    def image_tag(self, obj):
        if obj.partner_logo and obj.partner_logo.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.partner_logo.url
            )
        return "─"
    ordering = ('-id',)
admin.site.register(partners_logo, partners_logoAdmin)