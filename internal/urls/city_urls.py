from django.urls import path
from internal.views import city_views as views

urlpatterns = [
    path('', views.get_all_cities, name='rwa-cities'),
    path('<str:pk>', views.get_city_by_id, name='get-rwa-city-by-id')
]