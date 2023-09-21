from support.views import ticket_views as views
from django.urls import path

urlpatterns = [
    path('get/', views.get_all, name='get-all-tickets'),
    path('<str:pk>', views.get_one, name='get-one-ticket-as-per-user'),
    path('add/', views.add, name = 'add-ticket-request'),
]