from django.urls import path
from reporting.views.sale_history_views import SaleHistoryCreateView, OrderCreateView

urlpatterns = [
    path('history/', SaleHistoryCreateView.as_view(), name='sale-history'),
    path('order/', OrderCreateView.as_view(), name='order-details')
]
