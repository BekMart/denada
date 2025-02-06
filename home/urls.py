from django.urls import path
from . import views

# Define URL patterns for the home app
urlpatterns = [
    path('', views.homepage, name='home'),  # Route for contact page
]
