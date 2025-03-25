from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import About, Project, Pricing
from .forms import ContactForm

def index(request):
    projects = Project.objects.all().order_by('-created')[:4]
    return render(request, 'core/index.html', {'projects': projects})

def about(request):
    about_info = About.objects.first()
    return render(request, 'core/about.html', {'about': about_info})

def projects(request):
    projects = Project.objects.all().order_by('-created')
    return render(request, 'core/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def pricing(request):
    pricing_list = Pricing.objects.all()
    return render(request, 'core/pricing.html', {'pricing_list': pricing_list})