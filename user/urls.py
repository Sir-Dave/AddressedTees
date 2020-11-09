from django.urls import path
from user.views import RegistrationView

app_name = "users"
urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
]