from django.urls import path
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
    PasswordResetView
)
from member.views import member_views as views

urlpatterns = [
    path('', views.get_all_members, name='rwa-member-listing'),
    path('<str:pk>', views.get_member, name = 'view_member'),
    path('otp/', views.generate_otp, name='generate-otp'),
    path('verify/', views.verify_jwt, name='verify-jwt'),
    path('register/', views.register_member, name='register-member'),
    path('login/', views.login_member, name='login-member'),
    path('reset/', views.reset_password, name='reset-password'),
    # path('send-email/', views.send_email_to_client, name='send-email'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
