from . import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('mail', views.mail, name='mail'),
    path('sms', views.sms, name='sms'),
]