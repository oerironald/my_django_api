from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get),
    # path('push', views.make_payment),
    # path('', views.get),
    # path('index/<str:phone_number>/<int:amount>/', views.index, name='index'),
    # path('pay', views.stk_push_callback, name='mpesa_stk_push_callback'),
    path('payment', views.payment_form, name='payment'),
    path('paymentpro', views.process_payment, name='paymentpro'),
   # path('extract', views.extract_fields, name='extract_fields'),
]