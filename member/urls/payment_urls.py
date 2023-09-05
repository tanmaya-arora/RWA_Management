from django.urls import path
from member.views import payment_views as views

urlpatterns = [
    path('get_token/', views.generate_paytm_token, name='getTransactionToken'),
    path('verify_checksum/',views.verify_checksum, name='verify_checksum'),
    path('callback/', views.paytm_callback, name='payment_callback'),
]
