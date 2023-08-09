from member.views import cart_views as views
from django.urls import path

urlpatterns = [
    path('add/',views.cart_details,name='cart_details'),
    # path('add/', views.add_to_cart, name='add-to-cart')
]