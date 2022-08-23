"""car_rental_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from frontend import views as front
admin.site.site_header = 'CRB Admin'
admin.site.site_title = 'CRB Admin Panel'
admin.site.index_title = 'Welcome to CRB Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front.home, name="home"),
    path('about/', front.about, name="about"),
    path('contact/', front.contact, name="contact"),
    path('saveContact/', front.saveContact, name="saveContact"),
    path('vehicles/', front.vehicles, name="vehicles"),
    path('vehicle_details/<vehicleid>', front.vehicleDetails, name="vehicleDetails"),
    path('book_now/<int:car_id>', front.bookNow, name="bookNow"),
    path('services/', front.services, name="services"),
    path('login/', front.handleLogin, name="login"),
    path('signup/', front.handleSignup, name="signup"),
    path('logout/', front.handleLogout, name="logout"),
]
