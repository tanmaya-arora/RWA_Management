from member.views import package_attributes_views as views
from django.urls import path

urlpatterns = [
    path('',views.create_attributes ,name='create_attributes')
]
