from django.contrib import admin
from .models import Contact_item, contact_map

# Register your models here.
class Contact_list(admin.ModelAdmin):
    
    list_display = ['id', 'con_title', 'con_address','con_phone', 'con_email', 'con_descrip', 'created_at']
    list_display_links = ['id', 'con_title', 'con_address','con_phone', 'con_email', 'con_descrip']
    search_fields = ['id','con_title', 'con_address','con_phone', 'con_email']
    list_filter = ['created_at']
    ordering = ['id']
admin.site.register(Contact_item, Contact_list)

class Contact_map_list(admin.ModelAdmin):
    list_display = ['id', 'map_iframe', 'created_at']
    list_display_links = ['id', 'map_iframe']
    search_fields = ['id', 'map_iframe']
    list_filter = ['created_at']
    ordering = ['id']
admin.site.register(contact_map, Contact_map_list)