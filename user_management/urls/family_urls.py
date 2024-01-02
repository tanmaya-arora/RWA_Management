from django.urls import path
from user_management.views import family_views as views

urlpatterns = [
    path('',views.get_family_members,name='get-family-members'),
    path('<str:pk>', views.get_sepecific_family, name = 'get-familydetails'),
    path('register/',views.register_family_member,name='register-family-member')
]