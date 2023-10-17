from django.shortcuts import render
from .models import Product
import requests

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})