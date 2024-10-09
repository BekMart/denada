from . import views
from django.urls import path

urlpatterns = [
    path('', views.FoodList.as_view(), name='menu'),
    path('', views.DrinkList.as_view(), name='menu'),
]