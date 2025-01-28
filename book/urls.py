from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name='book'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]