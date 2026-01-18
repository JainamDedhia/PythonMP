"""
File: helpdesk/views.py
Replace the content of helpdesk/views.py with this code
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import WelfareScheme, Complaint, NGO, GovernmentOffice, UserProfile

def home(request):
    schemes = WelfareScheme.objects.all()[:6]
    context = {
        'schemes': schemes,
        'total_schemes': WelfareScheme.objects.count(),
        'total_ngos': NGO.objects.count(),
    }
    return render(request, 'helpdesk/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            UserProfile.objects.create(user=user, phone=phone, address=address)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def schemes_list(request):
    category = request.GET.get('category', '')
    if category:
        schemes = WelfareScheme.objects.filter(category=category)
    else:
        schemes = WelfareScheme.objects.all()
    
    categories = WelfareScheme.CATEGORY_CHOICES
    context = {
        'schemes': schemes,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'helpdesk/schemes_list.html', context)

def scheme_detail(request, pk):
    scheme = get_object_or_404(WelfareScheme, pk=pk)
    return render(request, 'helpdesk/scheme_detail.html', {'scheme': scheme})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        category = request.POST.get('category')
        
        Complaint.objects.create(
            user=request.user,
            subject=subject,
            description=description,
            category=category
        )
        messages.success(request, 'Complaint submitted successfully!')
        return redirect('my_complaints')
    
    return render(request, 'helpdesk/submit_complaint.html')

@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'helpdesk/my_complaints.html', {'complaints': complaints})

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    return render(request, 'helpdesk/complaint_detail.html', {'complaint': complaint})

def ngo_list(request):
    ngos = NGO.objects.all()
    return render(request, 'helpdesk/ngo_list.html', {'ngos': ngos})

def ngo_detail(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    return render(request, 'helpdesk/ngo_detail.html', {'ngo': ngo})

def office_list(request):
    offices = GovernmentOffice.objects.all()
    return render(request, 'helpdesk/office_list.html', {'offices': offices})

def office_detail(request, pk):
    office = get_object_or_404(GovernmentOffice, pk=pk)
    return render(request, 'helpdesk/office_detail.html', {'office': office})

@login_required
def dashboard(request):
    user_complaints = Complaint.objects.filter(user=request.user)
    context = {
        'total_complaints': user_complaints.count(),
        'pending_complaints': user_complaints.filter(status='pending').count(),
        'resolved_complaints': user_complaints.filter(status='resolved').count(),
        'recent_complaints': user_complaints.order_by('-created_at')[:5]
    }
    return render(request, 'helpdesk/dashboard.html', context)