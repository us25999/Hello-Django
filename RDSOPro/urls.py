
from django.urls import path
from . import views



urlpatterns = [
    path('user/<int:pk>', views.user_api, name="user_api"),
    path('complaint', views.complaint_registration, name="complaint_registration"),
]