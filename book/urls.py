from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name='book'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]