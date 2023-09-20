from marketing.views import donation_views as views
from django.urls import path

urlpatterns = [
    path('',views.get_all_donations,name='donation-details'),
    path('add/', views.add_donation, name='add-donation')
]