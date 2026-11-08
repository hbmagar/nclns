from django import forms 
from django.core.exceptions import ValidationError
from .models import client_contact_list
import re

class ClientContactForm(forms.ModelForm):
    class Meta:
        model = client_contact_list
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Name",
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Email",
                'required': 'required',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Phone Number",
                'required': 'required',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Message",
                'rows': 5,
                'required': 'required',
            }),
        }  
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise ValidationError('Name can only contain letters and spaces')
        return name
     
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^(\+977|977)?9[0-9]{9}$', phone):
            raise ValidationError('Enter a valid Nepali phone number')
        return phone    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[a-z0-9]([a-z0-9]{4,28}[a-z0-9])?@gmail\.com$'
        if not re.match(pattern, email.lower()):
            raise ValidationError('Enter a valid Gmail address')
        return email
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 255:
            raise ValidationError('Message must be at least 255 characters long')
        return message
    def clean(self):
        return super().clean()
    