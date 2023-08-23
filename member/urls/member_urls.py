from django.urls import path
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
    PasswordResetView
)
from member.views import member_views as views

urlpatterns = [
    path('', views.get_all_members, name='rwa-members-listing'),
    path('register/', views.register_member, name='add-rwa-member'),
    path('register-email/', views.send_email_to_client, name='registration-email-confirmation'),
    path('login/', views.login_member, name='rwa-member-login'),
    path('password_reset/', views.reset_password, name='password_reset'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]