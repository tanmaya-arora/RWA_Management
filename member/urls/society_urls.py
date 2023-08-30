from django.urls import path
from member.views import society_views as views

urlpatterns = [
    path('', views.get_all_societies, name='rwa-society-listing'),
    path('<str:pk>', views.get_society_by_id, name='rwa-society-listing-by-id')
]