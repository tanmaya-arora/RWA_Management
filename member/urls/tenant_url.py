from django.urls import path
from member.views import tenant_views as views 


urlpatterns =[
    path('',views.get_all_tenant,name='rwa-tenant-listing')
]

