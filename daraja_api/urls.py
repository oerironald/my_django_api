from django.urls import path
from . import views

urlpatterns = [
    path('', views.get),
    path('push', views.make_payment),
    path('', views.get),
]