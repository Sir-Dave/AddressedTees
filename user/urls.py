from django.urls import path
from user.views import RegistrationView
from rest_auth.views import LoginView, LogoutView, \
    PasswordResetConfirmView, PasswordResetView, PasswordChangeView

app_name = "users"
urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password/reset/', PasswordResetView.as_view()),
    path('password/reset/confirm', PasswordResetConfirmView.as_view()),
    path('password/change/', PasswordChangeView.as_view())


]