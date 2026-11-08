from django.db import models
from django.core.exceptions import ValidationError
import os

# Create your models here.
class Gallery_Item(models.Model):
    class Meta:
        db_table = 'gallery_item'
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"
    gallery_title = models.CharField(max_length=100)
    image_descriptions = models.TextField()
    gallery_image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery Item {self.id} - {self.gallery_title}"
    def clean_gallery_title(self):
        if len(self.gallery_title) > 50:
            raise ValidationError("Title must be less than 50 characters long.")
    def clean_image_descriptions(self):
        if len(self.image_descriptions) > 100:
            raise ValidationError("Image Descriptions must be less than 100 characters long.")
    def validate_image(gallery_image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(gallery_image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if gallery_image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
        
    def clean(self):
        self.clean_gallery_title()
        self.clean_image_descriptions()
        super().clean() 
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)
    