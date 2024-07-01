from django.urls import path
from .views import DashboardView, FinanceDashboardView, generate_excel
from . import views

urlpatterns = [
    path('', views.dashboard_base, name='dashboard_base'),
    path('dash', DashboardView.as_view(), name='dashboard'),
    path('finance/', FinanceDashboardView.as_view(), name='finance_dashboard'),
    path('dashboards', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('generate_excel/', views.generate_excel, name='generate_excel'),
    
]