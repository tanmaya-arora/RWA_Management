from reporting.views import stock_views as views
from django.urls import path

urlpatterns = [
    path('all/', views.get_all, name = 'get-all-products'),
    path('<str:pk>', views.get_stock_name, name = 'get-specific-product-details'),
]