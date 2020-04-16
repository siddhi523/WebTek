from . import views 
#from views import home
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('',views.home, name='home'),
    ]
