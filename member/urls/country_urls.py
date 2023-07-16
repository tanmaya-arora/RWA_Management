from django.urls import path
from member.views import country_views as views

urlpatterns = [
    path('', views.get_all_countries, name='country-listing')
]