from django.urls import path
from member.views import event_views as views

urlpatterns = [
    path('', views.get_events, name='event-listing')
]