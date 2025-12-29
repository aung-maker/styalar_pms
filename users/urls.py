from django.urls import path
from .views import RequestAccountView, LoginView

urlpatterns = [
    path('register-request/', RequestAccountView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]