from internal.views import cart_views as views
from django.urls import path

urlpatterns = [
    path('',views.get_cart_items,name='cart_details'),
    path('<str:pk>', views.get_cart_items_by_user, name='cart-items-by-user'),
    path('add/', views.cart_details, name='add-to-cart'),
    path('<str:id>/remove/',views.remove_items, name='remove_item')
]