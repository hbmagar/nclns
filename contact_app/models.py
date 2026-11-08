from django.db import models 
from django.core.exceptions import ValidationError
import re



"""=====contact part model====="""
class Contact_item(models.Model):
    class Meta:
        db_table = 'contact'
        verbose_name = "Contact Content"
        verbose_name_plural = "Contact Contents"
    con_title = models.CharField(max_length=100)
    con_descrip = models.TextField()
    con_address = models.CharField(max_length=255)
    con_email = models.EmailField()
    con_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Content {self.id} - {self.con_descrip} - {self.con_title}"
    
    def clean(self):
        if Contact_item.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 contact content.")
        super().clean()
    
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

    def validate_nepali_phone(phone):
        if not re.match(r'^(\+977|977)?9[0-9]{9}$', phone):
            raise ValidationError('Enter a valid Nepali phone number')
        
    def validate_gmail(email):
        pattern = r'^[a-z0-9]([a-z0-9]{4,28}[a-z0-9])?@gmail\.com$'
        if not re.match(pattern, email.lower()):
            raise ValidationError('Enter a valid Gmail address')
        
class contact_map(models.Model):
    class Meta:
        db_table = 'contact_map'
        verbose_name = "Contact Map"
        verbose_name_plural = "Contact Maps"
    map_iframe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Map {self.id} - {self.map_iframe}"
    
    def clean(self):
        if contact_map.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 contact map.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)
    
class client_contact_list(models.Model):
    class Meta:
        db_table = 'contact_send'
        verbose_name = "Contact Send"
        verbose_name_plural = "Contact Sends"
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Contact Send {self.id} - {self.name} - {self.email}"
    def validate_nepali_phone(phone):
        if not re.match(r'^(\+977|977)?9[0-9]{9}$', phone):
            raise ValidationError('Enter a valid Nepali phone number')
    def validate_gmail(email):
        pattern = r'^[a-z0-9]([a-z0-9]{4,28}[a-z0-9])?@gmail\.com$'
        if not re.match(pattern, email.lower()):
            raise ValidationError('Enter a valid Gmail address')
    def clean(self):
        self.validate_nepali_phone(self.phone)
        self.validate_gmail(self.email)
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)
    def get_short_message(self):
        return (self.message[:75] + '...') if len(self.message) > 75 else self.message
    
    