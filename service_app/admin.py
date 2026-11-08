from django.contrib import admin
from service_app.models import *
from django.utils.html import format_html
# Register your models here.

class ServiceAboutHeadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_about_header', 'service_about_discription')
    list_display_links = ('id', 'service_about_header', 'service_about_discription')
    search_fields = ('service_about_header',)
    list_filter = ('service_about_header',)
    ordering = ('id',)
admin.site.register(service_about_heading, ServiceAboutHeadingAdmin)

class ServiceProgressAriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'progress_heading', 'progress_percentage')
    list_display_links = ('id', 'progress_heading', 'progress_percentage')
    search_fields = ('progress_heading',)
    list_filter = ('progress_heading',)
    ordering = ('id',)
admin.site.register(service_progress_aria, ServiceProgressAriaAdmin)

class FeatureTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'feature_title', 'feature_discription', 'feature_short', 'feature_bold_text', 'created_at')
    list_display_links = ('id', 'feature_title', 'feature_discription', 'feature_short', 'feature_bold_text')
    search_fields = ('feature_title',)
    list_filter = ('created_at',)
    ordering = ('id',)
admin.site.register(feature_title, FeatureTitleAdmin)


class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'feature_heading','feature_icon', 'feature_description')
    list_display_links = ('id', 'feature_heading', 'feature_icon', 'feature_description')
    search_fields = ('feature_heading',)
    list_filter = ('feature_heading',)
    ordering = ('id',)
admin.site.register(service_feature, ServiceFeatureAdmin)

class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_contact_title', 'service_contact_heading', 'service_contact_description')
    list_display_links = ('id', 'service_contact_title', 'service_contact_heading', 'service_contact_description')
    search_fields = ('service_contact_heading',)
    list_filter = ('service_contact_heading',)
    ordering = ('id',)
admin.site.register(service_Contact, ServiceContactAdmin)