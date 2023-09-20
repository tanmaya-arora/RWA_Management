from django.urls import path
from internal.views import committee_views as views

urlpatterns = [
    path('', views.get_all_committees, name='rwa-committees')
]