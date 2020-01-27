from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'authentication'
urlpatterns = [
    # Create a user
    path('users/', RegistrationAPIView.as_view()),
    # Login a user
    path('users/login', LoginAPIView.as_view()),
    # Edit a user
    path('user', UserRetrieveUpdateAPIView.as_view()),
]
