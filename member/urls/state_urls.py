from django.urls import path
from member.views import state_views as views

urlpatterns = [
    path('', views.get_all_states, name='rwa-states-listing'),
    path('<str:pk>', views.get_state_by_id, name='rwa-state-listing-by-id')
]