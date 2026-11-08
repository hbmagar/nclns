from django.contrib import admin
from django.utils.html import format_html

"""include all models here"""
from home_app.models import *  



class index_items(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slide_items', 'event_btn', 'created_at', 'user' )
    list_display_links = ('id', 'title', 'description', 'slide_items', 'event_btn')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('id',)
    def slide_items(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
admin.site.register(index_slide, index_items)


class our_business_data(admin.ModelAdmin):
    list_display = ('id', 'title', 'main_title', 'description', 'image_tag', 'created_at')
    list_display_links = ('id', 'title', 'main_title', 'description', 'image_tag')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('id',)
    def image_tag(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
admin.site.register(our_business, our_business_data)

class moitive_list(admin.ModelAdmin):
    list_display = ('id', 'motive', 'motive_icon', 'created_at')
    list_display_links = ('id', 'motive', 'motive_icon')
    search_fields = ('motive',)
    list_filter = ('motive',)
    ordering = ('id',)
admin.site.register(busisness_motive_list, moitive_list)

class latest_product_list(admin.ModelAdmin):
    list_display = ('id', 'title', 'latest_product_image', 'created_at')
    list_display_links = ('id', 'title', 'latest_product_image')
    search_fields = ('title',)
    list_filter = ('title',)
    def latest_product_image(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ('id',)
admin.site.register(latest_product, latest_product_list)

class news_portal_list(admin.ModelAdmin):
    list_display = ('id', 'news_header','news_image', 'news', 'address', 'publisher_name', 'publish_date')
    list_display_links = ('id', 'news_header', 'news_image', 'news', 'address', 'publisher_name', 'publish_date')
    search_fields = ('news_header',)
    list_filter = ('news_header',)
    def news_image(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ('id',)
admin.site.register(news_portal, news_portal_list)



class event_part_list(admin.ModelAdmin):
    list_display = ('id', 'event_header','event_news', 'event_address', 'event_image', 'publish_date')
    list_display_links = ('id', 'event_header','event_news', 'event_address', 'event_image', 'publish_date')
    search_fields = ('event_header',)
    list_filter = ('event_header',)
    def event_image(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ('id',)
admin.site.register(event_part, event_part_list)

class experience_part_list(admin.ModelAdmin):
    list_display = ('id', 'experience_title', 'experience_number', 'experience_icon')
    list_display_links = ('id', 'experience_title', 'experience_number', 'experience_icon')
    search_fields = ('experience_title',)
    list_filter = ('experience_title',)
    ordering = ('id',)
admin.site.register(experience_part, experience_part_list)

class feed_back_list(admin.ModelAdmin):
    list_display = ('id', 'feedback_header', 'name', 'designation', 'feedback', 'feed_back_image')
    list_display_links = ('id', 'feedback_header', 'name', 'designation', 'feedback', 'feed_back_image')
    search_fields = ('feedback_header',)
    list_filter = ('feedback_header',)
    def feed_back_image(self, obj):
        if obj.image and obj.image.url:
            return format_html(
                '<img src="{}" height="80" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "─"
    ordering = ('id',)
admin.site.register(feed_back, feed_back_list)
