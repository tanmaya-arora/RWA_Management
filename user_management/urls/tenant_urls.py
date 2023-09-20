from django.urls import path
from user_management.views import tenant_views as views


urlpatterns =[
    path('',views.get_all_tenant,name='rwa-tenant-listing'),
    path('<str:pk>',views.get_tenant, name = 'tenat_details'),
    path('register/',views.register_tenant,name='add-rwa-tenant'),
    path('otp/', views.generate_otp, name='generate-otp'),
    path('verify/', views.verify_jwt, name='verify-jwt'),
    path('login/', views.login_tenant, name='login-member'),
    path('reset/', views.reset_password, name='reset-password'),
]