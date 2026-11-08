from django.db import models
from django.core.exceptions import ValidationError
import re
import os
# Create your models here.
class tabar(models.Model):
    class Meta:
        verbose_name = "Header App"
        verbose_name_plural = "Header Apps"
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='img/')
    scrolled_logo = models.ImageField(upload_to='img/', null=True, blank=True)
    company_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.address
    def address_clean(self):
        if len(self.address) > 100:
            raise ValidationError("Address must be less than 100 characters long.")
    def validate_nepali_phone(phone):
        if not re.match(r'^(\+977|977)?9[0-9]{9}$', phone):
            raise ValidationError('Enter a valid Nepali phone number')
        
    def validate_gmail(email):
        pattern = r'^[a-z0-9]([a-z0-9]{4,28}[a-z0-9])?@gmail\.com$'
        if not re.match(pattern, email.lower()):
            raise ValidationError('Enter a valid Gmail address')
    def validate_logo(logo):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(logo.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if logo.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Logo file size must be under 2MB.")
        
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        self.address_clean()

