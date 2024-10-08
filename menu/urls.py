from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu_page, name='menu'),
    path('drinks/', views.DrinkList.as_view(), name='menu'),
]