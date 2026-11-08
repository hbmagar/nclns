from django.db import models 
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone
import re
import os


"""
==================================
Index part
==================================
"""
# Slide Content Model
class index_slide(models.Model):
    class Meta:
        db_table = 'index_slide'
        verbose_name = "Slide Item"
        verbose_name_plural = "Slide Items"
        ordering = ['-created_at']
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='slides/', blank=False, null=False)
    event_btn = models.CharField(max_length=12, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}, {self.description}"
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def clean(self):
        if index_slide.objects.count() >= 4 and not self.pk:
            raise ValidationError("Cannot add more than 4 slide contents.")
        super().clean()

# Our Business Content Model
class our_business(models.Model):
    class Meta:
        db_table = 'our_business'
        verbose_name = "Our Business Item"
        verbose_name_plural = "Our Business Items"
        ordering = ['-created_at']
    title = models.CharField(max_length=100, blank=False, null=False)
    main_title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='img/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    
    def __str__(self):
        return f"{self.title}, {self.main_title}"
    
    def validate_title(self):
        if len(self.title) > 100:
            raise ValidationError("Title must be less than 100 characters long.")
    def validate_main_title(self):
        if len(self.main_title) > 150:
            raise ValidationError("Main Title must be less than 150 characters long.")
    def validate_description(self):
        if len(self.description) > 255:
            raise ValidationError("Description must be less than 255 characters long.")
    
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")

class busisness_motive_list(models.Model):
    class Meta:
        db_table = 'busisness_movitive_list'
        verbose_name = "Business Motive list Item"
        verbose_name_plural = "Business Motive Items"
        ordering = ['-created_at']
    our_business = models.ForeignKey(our_business, on_delete=models.CASCADE, related_name='motives')
    motive = models.CharField(max_length=100, blank=False, null=False)
    motive_icon = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f"{self.motive}"
    def validate_motive(self):
        if len(self.motive) > 100:
            raise ValidationError("Motive must be less than 100 characters long.")
    def validate_motive_icon(self):
        if len(self.motive_icon) > 50:
            raise ValidationError("Motive Icon must be less than 50 characters long.")
    def clean(self):
        if busisness_motive_list.objects.count() >= 4 and not self.pk:
            raise ValidationError("Cannot add more than 4 business motive contents.")
        super().clean()
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class latest_product(models.Model):
    class Meta:
        db_table = 'latest_product'
        verbose_name = "Latest Product Item"
        verbose_name_plural = "Latest Product Items"
        ordering = ['-created_at']
    title = models.CharField(max_length=25, blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"
    
    def validate_title(self):
        if len(self.title) > 25:
            raise ValidationError("Title must be less than 25 characters long.")
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")

class news_portal(models.Model):
    class Meta:
        db_table = 'news_portal'
        verbose_name = "News Item"
        verbose_name_plural = "News Items"
        ordering = ['-publish_date']
    news_header = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='news/', blank=False, null=False)
    news= models.TextField(blank=False, null=False)
    publish_date = models.DateField(auto_now_add=True, blank=False, null=False)
    publisher_name = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return f"{self.news_header}"
    def validate_news_header(self):
        if len(self.news_header) > 100:
            raise ValidationError("News Header must be less than 255 characters long.")
    def validate_address(self):
        if len(self.address) > 100:
            raise ValidationError("Address must be less than 100 characters long.")
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_news(self):
        if len(self.news) > 500:
            raise ValidationError("News content must be less than 500 characters long.")
    def clean(self):
        if news_portal.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 News contents.")
        super().clean()

class event_part(models.Model):
    class Meta:
        db_table = 'event_part'
        verbose_name = "Event Part Item"
        verbose_name_plural = "Event Part Items"
        ordering = ['-id']
    event_header = models.CharField(max_length=50, blank=False, null=False)
    event_news = models.CharField(max_length=100, blank=False, null=False)
    event_address = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='events/', blank=False, null=False)
    publish_date = models.DateField(auto_now_add=True, blank=False, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.event_header}"
    def validate_event_header(self):
        if len(self.event_header) > 50:
            raise ValidationError("Event Header must be less than 50 characters long.")
    def validate_event_news(self):
        if len(self.event_news) > 100:
            raise ValidationError("Event News must be less than 100 characters long.")
    def validate_event_address(self):
        if len(self.event_address) > 100:
            raise ValidationError("Event Address must be less than 100 characters long.")
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def clean(self):
        if event_part.objects.count() >= 3 and not self.pk:
            raise ValidationError("Cannot add more than 3 Event contents.")
        super().clean()

class experience_part(models.Model):
    class Meta:
        db_table = 'experience_part'
        verbose_name = "Experience Part Item"
        verbose_name_plural = "Experience Part Items"
        ordering = ['id']
    experience_icon = models.CharField(max_length=100, blank=False, null=False)
    experience_number = models.CharField(max_length=50, blank=False, null=False)
    experience_title = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return f"{self.experience_title}"
    def validate_experience_icon(self):
        if len(self.experience_icon) > 100:
            raise ValidationError("Experience Icon must be less than 100 characters long.")
    def validate_experience_number(self):
        if len(self.experience_number) > 500:
            raise ValidationError("Experience Number must be less than 500 characters long.")
    def validate_experience_title(self):
        if len(self.experience_title) > 100:
            raise ValidationError("Experience Title must be less than 100 characters long.")
    def clean(self):
        if experience_part.objects.count() >= 4 and not self.pk:
            raise ValidationError("Cannot add more than 4 Experience contents.")
        super().clean()

class feed_back(models.Model):
    class Meta:
        db_table = 'feed_back'
        verbose_name = "Feed Back Item"
        verbose_name_plural = "Feed Back Items"
        ordering = ['id']
    feedback_header = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    designation = models.CharField(max_length=100, blank=False, null=False)
    feedback = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='feedback/', blank=False, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.feedback_header}"
    def validate_feedback_header(self):
        if len(self.feedback_header) > 100:
            raise ValidationError("Feedback Header must be less than 100 characters long.")
    def validate_name(self):
        if len(self.name) > 100:
            raise ValidationError("Name must be less than 100 characters long.")
    def validate_designation(self):
        if len(self.designation) > 100:
            raise ValidationError("Designation must be less than 100 characters long.")
    def validate_feedback(self):
        if len(self.feedback) > 500:
            raise ValidationError("Feedback must be less than 500 characters long.")    
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def clean(self):
        if feed_back.objects.count() >= 100 and not self.pk:
            raise ValidationError("Cannot add more than 100 Feedback contents.")
        super().clean()