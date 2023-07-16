from django.urls import path
from member.views import committee_views as views

urlpatterns = [
    path('', views.get_all_committees, name='rwa-committees')
]