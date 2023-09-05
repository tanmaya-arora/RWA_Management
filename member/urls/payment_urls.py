from django.urls import path
from member.views import payment_views as views

urlpatterns = [
    path('get_token/', views.getTransactionToken, name='getTransactionToken'),
    # path('callback/', views.payment_callback, name='payment_callback'),
]
