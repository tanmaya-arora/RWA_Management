from django.urls import path
from internal.views import event_views as views

urlpatterns = [
    path('', views.get_events, name='event-listing')
]