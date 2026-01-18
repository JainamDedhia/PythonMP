"""
File: helpdesk/models.py
Replace the content of helpdesk/models.py with this code
"""

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12, blank=True)
    
    def __str__(self):
        return self.user.username

class WelfareScheme(models.Model):
    CATEGORY_CHOICES = [
        ('health', 'Health'),
        ('education', 'Education'),
        ('housing', 'Housing'),
        ('employment', 'Employment'),
        ('pension', 'Pension'),
        ('agriculture', 'Agriculture'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    eligibility = models.TextField()
    benefits = models.TextField()
    how_to_apply = models.TextField()
    official_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject} - {self.user.username}"

class NGO(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    website = models.URLField(blank=True)
    area_of_work = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class GovernmentOffice(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    office_hours = models.CharField(max_length=100)
    services_offered = models.TextField()
    
    def __str__(self):
        return self.name