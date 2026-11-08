from django.db import models
from django.core.exceptions import ValidationError
import re
import os


class footer_about(models.Model):
    class Meta:
        verbose_name = "Footer About"
        verbose_name_plural = "Footer About"
    full_company_name =  models.CharField(max_length=100, blank=False, null=False)
    company_slogan = models.CharField(max_length=100, blank=False, null=False)
    company_about = models.CharField(max_length=255, blank=False, null=False)
    copyright_date = models.DateField(auto_now_add=True, blank=False, null=False)
    copyright_name = models.CharField(max_length=50, blank=False, null=False)

    def clean(self):
        if footer_about.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 News contents.")
        super().clean()
def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
        if extension == 'svg':
        # Basic SVG validation - check if it's an XML file
            if not image.name.lower().endswith('.svg'):
                raise ValidationError("Invalid SVG file.")
            # You can add more SVG validation here if needed
            return
    
        # For other image types, use PIL to validate
        try:
            img = image.open(image)
            img.verify()
        except Exception:
            raise ValidationError("Upload a valid images. The file you uploaded was either not an image or a corrupted image.")
          
class recent_product_menu(models.Model):
    class Meta:
        verbose_name = "Recent Product"
        verbose_name_plural = "Recent Products"
    product_name = models.CharField(max_length=25, blank=False, null=False)
    image = models.ImageField(upload_to='img/', blank=True, null=True, verbose_name='Recent Product Image', validators=[validate_image] )
    
    
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")

    def clean(self):
        if recent_product_menu.objects.count() >= 5 and not self.pk:
            raise ValidationError("Cannot add more than 5 Product image.")
        super().clean()
    
