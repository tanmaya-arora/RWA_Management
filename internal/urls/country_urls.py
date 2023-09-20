from django.urls import path
from internal.views import country_views as views

urlpatterns = [
    path('', views.get_all_countries, name='country-listing'),
    path('<str:pk>', views.get_country_by_id, name='list-country-by-id')
]