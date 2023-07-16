from django.urls import path
from member.views import city_views as views

urlpatterns = [
    path('', views.get_all_cities, name='rwa-cities')
]