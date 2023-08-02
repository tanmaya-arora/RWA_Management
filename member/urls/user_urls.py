from member.views import user_views as views
from django.urls import path

urlpatterns=[
    path('', views.get_portal_users, name='portal-users'),
]