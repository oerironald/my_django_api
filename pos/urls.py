from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('pay/', views.process_payment, name='process_payment'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('check_product_name/', views.check_product_name, name='check_product_name'),  # Define this URL pattern
     path('check-stock/<int:pk>/', views.check_stock, name='check_stock'),
]