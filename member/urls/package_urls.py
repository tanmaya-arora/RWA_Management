from django.urls import path
from member.views import package_views as views

urlpatterns = [
    path('', views.package_details , name = 'package_details')
]
