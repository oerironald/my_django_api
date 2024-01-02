from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1,  name='index1'),
    path('canada2/', views.index2,  name='index2'),
    path('canada3/', views.index3,  name='index3'),
    
]