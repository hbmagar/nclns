from django.contrib import admin
from django.utils.html import format_html

"""include all models here"""
from about_team_app.models import *  

# Register your models here.
class TeamMember_title_partAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_title', 'sub_title')
    list_display_links = ('id', 'main_title', 'sub_title')
    list_filter = ('id', 'main_title', 'sub_title')
    ordering = ('id',)
admin.site.register(TeamMember_title_part, TeamMember_title_partAdmin)

class AdminTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_name', 'position', 'image_preview', 'facebook_link', 'twitter_link', 'whatsapp_link')
    list_display_links = ('id', 'admin_name', 'position','image_preview','facebook_link', 'twitter_link', 'whatsapp_link')
    list_filter = ('id', 'admin_name', 'position')
    def image_preview(self, obj):
        if obj.image and obj.image.url:
            return format_html('<img src="{}" style="width: 150px; height:150px;" />', format(obj.image.url))
        return "No Image"
    ordering = ('id',)
admin.site.register(AdminTeamMember, AdminTeamMemberAdmin)

class staffTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff_name', 'position', 'image_preview', 'facebook_link', 'twitter_link', 'whatsapp_link')
    list_display_links = ('id', 'staff_name', 'position','image_preview','facebook_link', 'twitter_link', 'whatsapp_link')
    def image_preview(self, obj):
        if obj.image and obj.image.url:
            return format_html('<img src="{}" style="width: 150px; height:150px;" />', format(obj.image.url))
        return "No Image"
    ordering = ('id',)
admin.site.register(staffTeamMember, staffTeamMemberAdmin)

