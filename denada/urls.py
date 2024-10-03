"""
URL configuration for denada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import homepage
from menu.views import menu_page
from book.views import booking_page
from contact.views import contact_page
from login.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('menu/', menu_page, name='menu'),
    path('book/', booking_page, name='book'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
]
