from member.views import cart_views as views
from django.urls import path

urlpatterns = [
    path('',views.get_cart_items,name='cart_details'),
    path('add/', views.cart_details, name='add-to-cart')
]