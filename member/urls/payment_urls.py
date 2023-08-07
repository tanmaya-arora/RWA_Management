from django.urls import path
from member.views import payment_views as views

urlpatterns = [
    path('',views.payment_views,name='payment_views'),
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('callback/', views.payment_callback, name='payment_callback'),
]
