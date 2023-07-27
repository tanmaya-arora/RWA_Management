from django.urls import path
from member.views import payment_views as views

urlpatterns = [
    path('',views.payment_views,name='payment_views')
]
