from django.urls import path
from member.views import tenant_views as views


urlpatterns =[
    path('',views.get_all_tenant,name='rwa-tenant-listing'),
    path('register/',views.register_tenant,name='add-rwa-tenant'),
    path('otp/', views.generate_otp, name='generate-otp'),
    path('verify-otp/', views.verify_otp, name='verify-otp')
]

