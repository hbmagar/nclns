from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone
import re
import os

# Create your models here.
class AboutUs(models.Model):
    class Meta:
        db_table = 'about_us'
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ['id']
    about_title = models.CharField(max_length=50, blank=False, null=False)
    about_header = models.CharField(max_length=100, blank=False, null=False) 
    about_us = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='about_us_images/')
    first_btn = models.CharField(max_length=20, blank=False, null=False)
    second_btn = models.CharField(max_length=20, blank=False, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.about_title
    def validavalidate_about_title(about_title):
        if not re.match(r'^[A-Za-z0-9\s]+$', about_title):
            raise ValidationError('About title can only contain letters, numbers, and spaces.')
    def validate_about_header(about_header):
        if not re.match(r'^[A-Za-z0-9\s]+$', about_header):
            raise ValidationError('About header can only contain letters, numbers, and spaces.')
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_first_btn(first_btn):
        if not re.match(r'^[A-Za-z0-9\s]+$', first_btn):
            raise ValidationError('First button text can only contain letters, numbers, and spaces.')
    def validate_second_btn(second_btn):
        if not re.match(r'^[A-Za-z0-9\s]+$', second_btn):
            raise ValidationError('Second button text can only contain letters, numbers, and spaces.')
    def clean(self):
        if AboutUs.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 About Us content.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class about_aims(models.Model):
    class Meta:
        db_table = 'about_aims'
        verbose_name = 'About Aims'
        verbose_name_plural = 'About Aims'
        ordering = ['id']
    about_aim_title = models.CharField(max_length=50, blank=False, null=False)
    about_aim= models.TextField(max_length=255, blank=False, null=False)
    about_aim_icon = models.CharField(max_length=100, blank=False, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.about_aim_title
    def validate_about_aim_title(about_aim_title):
        if not re.match(r'^[A-Za-z0-9\s]+$', about_aim_title):
            raise ValidationError('About aim title can only contain letters, numbers, and spaces.')
    def validate_about_aim(about_aim):
        if not re.match(r'^[A-Za-z0-9\s]+$', about_aim):
            raise ValidationError('About aim can only contain letters, numbers, and spaces.')
    def validate_about_aim_icon(about_aim_icon):
        if not re.match(r'^[A-Za-z0-9\s]+$', about_aim_icon):
            raise ValidationError('About aim icon can only contain letters, numbers, and spaces.')
    def clean(self):
        if about_aims.objects.count() >= 4 and not self.pk:
            raise ValidationError("Cannot add more than 4 About Aims content.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



class about_partners_header(models.Model):
    class Meta:
        db_table = 'about_partners_header'
        verbose_name = 'About Partners Header'
        verbose_name_plural = 'About Partners Header'
        ordering = ['id']
    partner_title = models.CharField(max_length=50, blank=False, null=False)
    partner_header = models.CharField(max_length=100, blank=False, null=False) 
    trust_type = models.CharField(max_length=50, blank=False, null=False)
    trust_icon = models.CharField(max_length=50, blank=False, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.partner_title
    def validate_partner_title(partner_title):
        if not re.match(r'^[A-Za-z0-9\s]+$', partner_title):
            raise ValidationError('Partner title can only contain letters, numbers, and spaces.')
    def validate_partner_header(partner_header):
        if not re.match(r'^[A-Za-z0-9\s]+$', partner_header):
            raise ValidationError('Partner header can only contain letters, numbers, and spaces.')
    def validate_trust_type(trust_type):
        if not re.match(r'^[A-Za-z0-9\s]+$', trust_type):
            raise ValidationError('Trust type can only contain letters, numbers, and spaces.')
    def validate_trust_icon(trust_icon):
        if not re.match(r'^[A-Za-z0-9\s]+$', trust_icon):
            raise ValidationError('Trust icon can only contain letters, numbers, and spaces.')
    def clean(self):
        if about_partners_header.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 About Partners Header content.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class partners_logo(models.Model):
    class Meta:
        db_table = 'partners_logo'
        verbose_name = 'Partners Logo'
        verbose_name_plural = 'Partners Logo'
        ordering = ['id']
    partner_logo = models.ImageField(upload_to='partners_logos/')
    id = models.AutoField(primary_key=True)
    
    def validate_partner_logo(partner_logo):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(partner_logo.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if partner_logo.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def clean(self):
        if partners_logo.objects.count() >= 100 and not self.pk:
            raise ValidationError("Cannot add more than 100 Partners Logo content.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
