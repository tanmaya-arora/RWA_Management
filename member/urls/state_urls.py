from django.urls import path
from member.views import state_views as views

urlpatterns = [
    path('', views.get_all_states, name='rwa-states-listing')
]