# users/urls.py

from allauth.account.views import signup, login, logout
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, profile, CustomPasswordResetView, CustomPasswordResetDoneView, \
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomEmailVerificationSentView, CustomEmailConfirmationView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', signup, name='account_signup'),
    path('login/', login, name='account_login'),
    path('logout/', logout, name='account_logout'),
    # Password Reset URLs using your custom views

    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),


    path('accounts/confirm-email/', CustomEmailVerificationSentView.as_view(), name='account_email_verification_sent'),

    path('accounts/confirm-email/<key>/', CustomEmailConfirmationView.as_view(), name='account_confirm_email'),


    # Profile URL (keeping your existing custom view)
    path('profile/', profile, name='profile'),

    path('accounts/', include('allauth.urls')),
]
