from django.shortcuts import render

# Create your views here.
from .models import FAQ

def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq.html', {'faqs': faqs})