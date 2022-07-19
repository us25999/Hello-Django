
from django.urls import path, include

from .views import *



urlpatterns = [
    path('user', user_api, name="user_api"),
    path('user/<int:pk>', user_api, name="user_api"),
]