from django.urls import path
from .views import FreelanceSignupView, ClientSignupView


urlpatterns = [
    path('signup/freelance/',FreelanceSignupView.as_view()),
    path('signup/client/',ClientSignupView.as_view()),
]

