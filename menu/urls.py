from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu_page, name='menu'),
    path('food/', views.FoodList.as_view(), name='food'),
    path('drink/', views.DrinkList.as_view(), name='drink'),
]