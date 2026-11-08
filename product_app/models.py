from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import os
import re

# Create your models here.

# Service Index Model
class about_product(models.Model):
    class Meta:
        db_table ='about_product'
        verbose_name = 'About Product'
        verbose_name_plural = 'About Products'
        ordering = ['id']
    product_about_header = models.CharField(max_length=150, blank=False, null=False, verbose_name='Second Title')
    product_focus_header = models.CharField(max_length=50, blank=False, null=False, verbose_name='Third Title')
    explain = models.TextField(max_length=255, blank=False, null=False, verbose_name='Explain')
    btn_text = models.CharField(max_length=50, blank=False, null=False, verbose_name='Button Text')
    img1 = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Service Image 1')
    img2 = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Service Image 2')
    img3 = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Service Image 3')
    img4 = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Service Image 4')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.product_about_header
    def validate_product_about_header(self):
         if len(self.product_about_header) > 150:
            raise ValidationError("Product About Header must be less than 150 characters long.")
    def validate_product_focus_header(self):
         if len(self.product_focus_header) > 50:
            raise ValidationError("Product Focus Header must be less than 50 characters long.")
    def clean(self):
        # Validate that all four images are provided
        if about_product.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 100 entries to about_product.")
        if not all([self.img1, self.img2, self.img3, self.img4]):
            raise ValidationError("All four images are required.")
        
        # Validate file types for each image
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        pixels = [self.img1, self.img2, self.img3, self.img4]
        
        for img in pixels:
            if img:
                extension = img.name.split('.')[-1].lower()
                if extension not in valid_extensions:
                    raise ValidationError(f"Only JPG, JPEG, PNG, and SVG files are allowed. Invalid file: {img.name}")
                
                if img.size > 2 * 1024 * 1024:  # 2MB limit
                    raise ValidationError(f"Image file size must be under 2MB. {img.name} is too large.")
        super().clean() 
class product_list(models.Model):
    class Meta:
        db_table ='product_list'
        verbose_name = 'Product List'
        verbose_name_plural = 'Product Lists'
        ordering = ['id']
    image = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Product Image')
    product_header = models.CharField(max_length=30, blank=False, null=False, verbose_name='Product Header')
    published_date = models.DateField(auto_now_add=True, verbose_name='Published Date')
    place = models.CharField(max_length=100, blank=False, null=False, verbose_name='Place')
    price = models.DecimalField(max_digits=10, decimal_places=1, blank=False, null=False, verbose_name='Price')
    star_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False, verbose_name='Star Rate')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.product_header
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_product_header(self):
         if len(self.product_header) > 30:
            raise ValidationError("Product Header must be less than 30 characters long.")
    def validate_place(self):
         if len(self.place) > 100:
            raise ValidationError("Place must be less than 100 characters long.")
    def validate_price(self):
        if self.price < 0:
            raise ValidationError("Price must be a positive number.")
    def validate_star_rate(self):
        if self.star_rate is not None and (self.star_rate < 0 or self.star_rate > 5):
            raise ValidationError("Star Rate must be between 0 and 5.")
    def clean(self):
        if product_list.objects.count() >= 500 and not self.pk:
            raise ValidationError("Cannot add more than 500 Product List entries.")
        super().clean()

class upcoming_product(models.Model):
    class Meta:
        db_table ='upcoming_product'
        verbose_name = 'Upcoming Product'
        verbose_name_plural = 'Upcoming Products'
        ordering = ['id']
    image = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Upcoming Product Image')
    product_header = models.CharField(max_length=30, blank=False, null=False, verbose_name='Upcoming Product Header')
    product_about = models.TextField(max_length=255, blank=False, null=False, verbose_name='Upcoming Product About')
    published_date = models.DateField(auto_now_add=True, verbose_name='Published Date')
    product_status = models.CharField(max_length=20, blank=False, null=False, verbose_name='Product Status')
    react_rate = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)], blank=False, null=False, verbose_name='React Rate')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Username')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.product_header
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_product_header(self):
         if len(self.product_header) > 30:
            raise ValidationError("Upcoming Product Header must be less than 30 characters long.")
    def validate_product_about(self):
         if len(self.product_about) > 255:
            raise ValidationError("Upcoming Product About must be less than 255 characters long.")
    def validate_product_status(self):
         if len(self.product_status) > 20:
            raise ValidationError("Product Status must be less than 20 characters long.")
    def clean(self):
        if upcoming_product.objects.count() >= 3 and not self.pk:
            raise ValidationError("Cannot add more than 3 Upcoming Product entries.")
        super().clean()

class deals_product(models.Model):
    class Meta:
        db_table ='deals_product'
        verbose_name = 'Deals Product'
        verbose_name_plural = 'Deals Products'
        ordering = ['id']
    image = models.ImageField(upload_to='img/', blank=False, null=True, verbose_name='Deals Product Image')
    deal_title = models.CharField(max_length=30, blank=False, null=False, verbose_name='Deals Product Title')
    deal_header = models.CharField(max_length=30, blank=False, null=False, verbose_name='Deals Product Header')
    deal_description = models.TextField(max_length=255, blank=False, null=False, verbose_name='Deals Product Description')
    deal_slogan = models.CharField(max_length=100, blank=False, null=False, verbose_name='Deals Product Slogan')
    facebook_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Facebook Link')
    google_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Google Link')
    whatsapp_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='WhatsApp Link')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.deal_title
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_deal_title(self):
         if len(self.deal_title) > 30:
            raise ValidationError("Deals Product Title must be less than 30 characters long.")
    def validate_deal_header(self):
         if len(self.deal_header) > 30:
            raise ValidationError("Deals Product Header must be less than 30 characters long.")
    def validate_deal_description(self):
         if len(self.deal_description) > 255:
            raise ValidationError("Deals Product Description must be less than 255 characters long.")
    def validate_deal_slogan(self):
         if len(self.deal_slogan) > 100:
            raise ValidationError("Deals Product Slogan must be less than 100 characters long.")
    def validate_facebook_link(self):
        if self.facebook_link and not re.match(r'^(https?://)?(www\.)?facebook\.com/.+$', self.facebook_link):
            raise ValidationError("Invalid Facebook URL.")
    def validate_google_link(self):
        if self.google_link and not re.match(r'^(https?://)?(www\.)?google\.com/.+$', self.google_link):
            raise ValidationError("Invalid Google URL.")
    def validate_whatsapp_link(self):
        if self.whatsapp_link and not re.match(r'^(https?://)?(www\.)?whatsapp\.com/.+$', self.whatsapp_link):
            raise ValidationError("Invalid WhatsApp URL.")
    def clean(self):
        if deals_product.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 Deals Product entries.")
        super().clean()
   