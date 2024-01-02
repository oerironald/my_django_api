from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index1(request):
    
    return render(request,'canada/index.html')


def index2(request):
    
    return render(request,'canada/index2.html') 



def index3(request):
    
    return render(request,'canada/index3.html')


def index4(request):
    
    return render(request,'canada/index4.html')




# Create your views here.
