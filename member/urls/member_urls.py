from django.urls import path
from member.views import member_views as views

urlpatterns = [
    path('', views.get_all_members, name='rwa-members-listing'),
    path('register/', views.register_member, name='add-rwa-member'),
    path('login/', views.login_member, name='rwa-member-login')
]