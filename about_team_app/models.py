from django.db import models 
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone
import re
import os

class TeamMember_title_part(models.Model):
    class Meta:
        db_table = "team_member_title_part"
        verbose_name = "Team Member Title Part"
        verbose_name_plural = "Team Member Title Parts"
    main_title = models.CharField(max_length=100, blank=False, null=False)
    sub_title = models.CharField(max_length=200, blank=False, null=False)
    focus_title = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.main_title
    def validate_main_title(self):
        if not re.match(r'^[A-Za-z0-9\s]+$', self.main_title):
            raise ValidationError("Main title can only contain letters, numbers, and spaces.")
    def validate_sub_title(self):
        if not re.match(r'^[A-Za-z0-9\s]+$', self.sub_title):
            raise ValidationError("Sub title can only contain letters, numbers, and spaces.")
    def clean(self):
        if TeamMember_title_part.objects.count() >= 1 and not self.pk:
            raise ValidationError("Cannot add more than 1 team member title part.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class AdminTeamMember(models.Model):
    class Meta:
        db_table = "admin_team_member"
        verbose_name = "Admin Team Member"
        verbose_name_plural = "Admin Team Members"
        ordering = ['id']
    admin_name = models.CharField(max_length=100, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='team_members/')
    facebook_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_link = models.URLField(max_length=255, blank=True, null=True)
    whatsapp_link = models.URLField(max_length=255, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.admin_name
    def validate_admin_name(self):
        if not re.match(r'^[A-Za-z\s]+$', self.admin_name):
            raise ValidationError("Admin name can only contain letters and spaces.")
    def validate_position(self):
        if not re.match(r'^[A-Za-z\s]+$', self.position):
            raise ValidationError("Position can only contain letters and spaces.")
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_facebook_link(self):
        if self.facebook_link and not re.match(r'^(https?://)?(www\.)?facebook\.com/.+$', self.facebook_link):
            raise ValidationError("Invalid Facebook URL.")
    def validate_twitter_link(self):
        if self.twitter_link and not re.match(r'^(https?://)?(www\.)?twitter\.com/.+$', self.twitter_link):
            raise ValidationError("Invalid Twitter URL.")
    def validate_whatsapp_link(self):
        if self.whatsapp_link and not re.match(r'^(https?://)?(www\.)?whatsapp\.com/.+$', self.whatsapp_link):
            raise ValidationError("Invalid WhatsApp URL.")
    def clean(self):
        if AdminTeamMember.objects.count() >= 100 and not self.pk:
            raise ValidationError("Cannot add more than 100 admin team members.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class staffTeamMember(models.Model):
    class Meta:
        db_table = "staff_team_member"
        verbose_name = "Staff Team Member"
        verbose_name_plural = "Staff Team Members"
        ordering = ['id']
    staff_name = models.CharField(max_length=100, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='team_members/')
    facebook_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_link = models.URLField(max_length=255, blank=True, null=True)
    whatsapp_link = models.URLField(max_length=255, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.staff_name
    def validate_staff_name(self):
        if not re.match(r'^[A-Za-z\s]+$', self.staff_name):
            raise ValidationError("Staff name can only contain letters and spaces.")
    def validate_position(self):
        if not re.match(r'^[A-Za-z\s]+$', self.position):
            raise ValidationError("Position can only contain letters and spaces.")
    def validate_image(image):
        valid_extensions = ['jpg', 'jpeg', 'png', 'svg']
        extension = os.path.splitext(image.name)[1][1:].lower()
        if extension not in valid_extensions:
            raise ValidationError("Only JPG, JPEG, PNG, and SVG files are allowed.")
        if image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError("Image file size must be under 2MB.")
    def validate_facebook_link(self):
        if self.facebook_link and not re.match(r'^(https?://)?(www\.)?facebook\.com/.+$', self.facebook_link):
            raise ValidationError("Invalid Facebook URL.")
    def validate_twitter_link(self):
        if self.twitter_link and not re.match(r'^(https?://)?(www\.)?twitter\.com/.+$', self.twitter_link):
            raise ValidationError("Invalid Twitter URL.")
    def validate_whatsapp_link(self):
        if self.whatsapp_link and not re.match(r'^(https?://)?(www\.)?whatsapp\.com/.+$', self.whatsapp_link):
            raise ValidationError("Invalid WhatsApp URL.")
    def clean(self):
        if staffTeamMember.objects.count() >= 100 and not self.pk:
            raise ValidationError("Cannot add more than 100 staff team members.")
        super().clean()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    