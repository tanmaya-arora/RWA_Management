from internal.views import package_category_views as views
from django.urls import path

urlpatterns=[
    path('', views.get_package_categories, name='package_categories'),
    path('<str:pk>',views.get_package, name='view_category'),
    path('filter-package-categories/', views.get_package_categories_by_user_type, name='package-categories-by-user')
]