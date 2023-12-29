from django.shortcuts import render

def index(request):
    return render(request, 'canada/index.html')

# Create your views here.
