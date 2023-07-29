from django.urls import path
from member.views import family_views as views

urlpatterns = [
    path('',views.get_family_members,name='get-family-members'),
    path('register/',views.family_member,name='register-family-member')
]