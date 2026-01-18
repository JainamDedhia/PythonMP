"""
File: helpdesk/urls.py
CREATE this NEW FILE in helpdesk folder
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('schemes/', views.schemes_list, name='schemes_list'),
    path('schemes/<int:pk>/', views.scheme_detail, name='scheme_detail'),
    
    path('complaints/submit/', views.submit_complaint, name='submit_complaint'),
    path('complaints/my/', views.my_complaints, name='my_complaints'),
    path('complaints/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    
    path('ngos/', views.ngo_list, name='ngo_list'),
    path('ngos/<int:pk>/', views.ngo_detail, name='ngo_detail'),
    
    path('offices/', views.office_list, name='office_list'),
    path('offices/<int:pk>/', views.office_detail, name='office_detail'),
]