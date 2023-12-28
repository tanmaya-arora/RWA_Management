from django.urls import path
from internal.views import payment_views as views

urlpatterns = [
    path('', views.get_all_payments, name='payment-listing'),
    path('<str:pk>', views.get_active_user_payments, name='filter-payments-by-active-user'),
    path('add/', views.add_cash_or_bank_payment, name='addCashBankPayment'),
    path('get_token/', views.generate_paytm_token, name='getTransactionToken'),
    path('verify_checksum/',views.verify_checksum, name='verify_checksum'),
    path('callback/', views.paytm_callback, name='payment_callback'),
]
