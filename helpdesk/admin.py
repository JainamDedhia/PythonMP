"""
File: helpdesk/admin.py
Replace the content of helpdesk/admin.py with this code
"""

from django.contrib import admin
from .models import UserProfile, WelfareScheme, Complaint, NGO, GovernmentOffice

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'aadhar_number']
    search_fields = ['user__username', 'phone']

@admin.register(WelfareScheme)
class WelfareSchemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'category', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['subject', 'description', 'user__username']
    list_editable = ['status']

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'phone', 'area_of_work']
    search_fields = ['name', 'area_of_work']

@admin.register(GovernmentOffice)
class GovernmentOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'phone', 'email']
    search_fields = ['name', 'department']
    list_filter = ['department']