from django.db import models
from django.core.exceptions import ValidationError

class service_about_heading(models.Model):
    class Meta:
        db_table = 'service_about_heading'
        verbose_name = "Service About Heading"
        verbose_name_plural = "Service About Headings"
    service_about_header = models.CharField(max_length=255)
    service_about_discription = models.TextField(max_length=500)
    def __str__(self):
        return f"Service About Heading {self.id} - {self.service_about_header}"
    def clean_service_about_header(self):
        if not self.service_about_header:
            raise ValidationError("Service about header cannot be empty.")
    def clean_service_about_discription(self):
        if not self.service_about_discription:
            raise ValidationError("Service about description cannot be empty.")
        if len(self.service_about_discription) > 500:
            raise ValidationError("Service about description cannot exceed 500 characters.")
        return self.service_about_discription
    def clean_service_about_header(self):
        if not self.service_about_header:
            raise ValidationError("Service about header cannot be empty.")
        if len(self.service_about_header) > 255:
            raise ValidationError("Service about header cannot exceed 255 characters.")
        return self.service_about_header
    def clean_service_about_discription(self):
        if not self.service_about_discription:
            raise ValidationError("Service about description cannot be empty.")
        if len(self.service_about_discription) > 500:
            raise ValidationError("Service about description cannot exceed 500 characters.")
        return self.service_about_discription
    def clean(self):
        if service_about_heading.objects.count() >= 4 and not self.pk:
            raise ValidationError("Cannot add more than 4 Service About Headings.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

class service_progress_aria(models.Model):
    class Meta:
        db_table = 'service_progress_aria'
        verbose_name = "Service Progress Aria"
        verbose_name_plural = "Service Progress Arias"
    progress_heading = models.CharField(max_length=100)
    progress_percentage = models.IntegerField()
    def __str__(self):
        return f"Service Progress Aria {self.id} - {self.progress_heading}"
    def clean_progress_heading(self):
        if not self.progress_heading:
            raise ValidationError("Progress heading cannot be empty.")
        if len(self.progress_heading) > 100:
            raise ValidationError("Progress heading cannot exceed 100 characters.")
        return self.progress_heading
    def clean_progress_percentage(self):
        if self.progress_percentage is None:
            raise ValidationError("Progress percentage cannot be empty.")
        if not (0 <= self.progress_percentage <= 100):
            raise ValidationError("Progress percentage must be between 0 and 100.")
        return self.progress_percentage
    def clean(self):
        if service_progress_aria.objects.count() >= 3 and not self.pk:
            raise ValidationError("Cannot add more than 3 Service Progress Arias.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)
 
class feature_title(models.Model):
    class Meta:
        db_table = 'feature_title'
        verbose_name = "Feature Title"
        verbose_name_plural = "Feature Titles"
    feature_title = models.CharField(max_length=100)
    feature_discription = models.CharField(max_length=255)
    feature_short = models.CharField(max_length=100)
    feature_bold_text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Service Feature {self.id} - {self.feature_title}"
    def clean_feature_title(self):
        if not self.feature_title:
            raise ValidationError("Feature title cannot be empty.")
        if len(self.feature_title) > 100:
            raise ValidationError("Feature title cannot exceed 100 characters.")
        return self.feature_title
    def clean_feature_discription(self):
        if not self.feature_discription:
            raise ValidationError("Feature description cannot be empty.")
        if len(self.feature_discription) > 255:
            raise ValidationError("Feature description cannot exceed 255 characters.")
        return self.feature_discription
    def clean_feature_short(self):
        if not self.feature_short:
            raise ValidationError("Feature short cannot be empty.")
        if len(self.feature_short) > 100:
            raise ValidationError("Feature short cannot exceed 100 characters.")
        return self.feature_short
    def clean_feature_bold_text(self):
        if not self.feature_bold_text:
            raise ValidationError("Feature bold text cannot be empty.")
        if len(self.feature_bold_text) > 50:
            raise ValidationError("Feature bold text cannot exceed 50 characters.")
        return self.feature_bold_text
    def clean(self):
        if feature_title.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 Service Feature Titles.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

class service_feature(models.Model):
    class Meta:
        db_table = 'service_feature'
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"
        ordering = ['id']
    feature_heading = models.CharField(max_length=100)
    feature_description = models.TextField(max_length=255)
    feature_icon = models.CharField(max_length=100, help_text="Enter the CSS class for the icon, e.g., 'fa fa-star'")
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"Service Feature {self.id} - {self.feature_heading}"    
    def clean_feature_heading(self):
        if not self.feature_heading:
            raise ValidationError("Feature heading cannot be empty.")
        if len(self.feature_heading) > 100:
            raise ValidationError("Feature heading cannot exceed 100 characters.")
        return self.feature_heading
    def clean_feature_description(self):
        if not self.feature_description:
            raise ValidationError("Feature description cannot be empty.")
        if len(self.feature_description) > 255:
            raise ValidationError("Feature description cannot exceed 255 characters.")
        return self.feature_description
    def clean_feature_icon(self):
        if not self.feature_icon:
            raise ValidationError("Feature icon cannot be empty.")
        if len(self.feature_icon) > 100:
            raise ValidationError("Feature icon cannot exceed 100 characters.")
        return self.feature_icon
    def clean(self):
        if service_feature.objects.count() >= 6 and not self.pk:
            raise ValidationError("Cannot add more than 6 Service Features.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

class service_Contact(models.Model):
    class Meta:
        db_table = 'service_contact'
        verbose_name = "Service Contact"
        verbose_name_plural = "Service Contacts"
    service_contact_title = models.CharField(max_length=100)
    service_contact_heading = models.CharField(max_length=100)
    service_contact_description = models.TextField(max_length=255)
    def __str__(self):
        return f"Service Contact {self.id} - {self.service_contact_heading}"
    def clean_service_contact_heading(self):
        if not self.service_contact_heading:
            raise ValidationError("Service contact heading cannot be empty.")
        if len(self.service_contact_heading) > 100:
            raise ValidationError("Service contact heading cannot exceed 100 characters.")
        return self.service_contact_heading
    def clean_service_contact_description(self):
        if not self.service_contact_description:
            raise ValidationError("Service contact description cannot be empty.")
        if len(self.service_contact_description) > 255:
            raise ValidationError("Service contact description cannot exceed 255 characters.")
        return self.service_contact_description 
    def clean_service_contact_title(self):
        if not self.service_contact_title:
            raise ValidationError("Service contact title cannot be empty.")
        if len(self.service_contact_title) > 100:
            raise ValidationError("Service contact title cannot exceed 100 characters.")
        return self.service_contact_title
    def clean(self):
        if service_Contact.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 Service Contact.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean() method
        super().save(*args, **kwargs)

