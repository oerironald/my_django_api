from django.urls import path
from . import views

urlpatterns = [
    path('', views.streamlit_app),
    # Add other URL patterns for your Django application
]