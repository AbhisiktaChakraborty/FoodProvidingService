"""design_lab_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from raisemodifyorder.views import *


urlpatterns = [
   path('admin/', admin.site.urls),
   path('',displaySignInForm,name="signin"),
   path('signin.html',displaySignInForm,name="signin"),
   path('raiseorder.html', displayNewOrderForm, name='raiseorder'),
   path('modifyorder.html', displayEditableOrderForm, name='modifyorder'),
   path('dashboard_foodseeker.html', displayFSOrderList, name='dashboard_foodseeker'),
   path('raisemodifyorder/header.html',header, name='header'),
   path('dashboardfoodprovider.html',confirmOrder, name='confirmorder') 
]
