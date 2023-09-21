"""
URL configuration for RWA_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', include('admin_soft.urls')),
    path('admin/', admin.site.urls),
    path('api/cart/', include('internal.urls.cart_urls')),
    path('api/city/', include('internal.urls.city_urls')),
    path('api/committees/', include('internal.urls.committee_urls')),
    path('api/country/', include('internal.urls.country_urls')),
    path('api/donation/', include('marketing.urls.donation_urls')),
    path('api/events/', include('internal.urls.event_urls')),
    path('api/family-members/', include('user_management.urls.family_urls')),
    path('api/members/', include('user_management.urls.owner_urls')),
    path('api/package-categories/', include('internal.urls.package_category_urls')),
    path('api/payment/', include('internal.urls.payment_urls')),
    path("api/tenant/", include('user_management.urls.tenant_urls')),
    path('api/society/', include('internal.urls.society_urls')),
    path('api/ticket',include('support.urls.ticket_urls')),
    path('api/states/', include('internal.urls.state_urls')),
    path('api/users/', include('internal.urls.user_urls')),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh')
]
