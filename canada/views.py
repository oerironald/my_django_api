from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index1(request):
    
    return render(request,'index.html')

# Create your views here.
