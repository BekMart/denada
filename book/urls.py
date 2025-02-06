from django.urls import path
from . import views

# Define URL patterns for the booking app
urlpatterns = [
    path('', views.booking_page, name='book'),  # Route for booking page
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),  # Route for editing an existing booking
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),  # Route for canceling a booking
]
