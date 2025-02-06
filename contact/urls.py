from django.urls import path
from . import views

# Define URL patterns for the contact app
urlpatterns = [
    path('', views.contact_page, name='contact'),  # Route for contact page
]
