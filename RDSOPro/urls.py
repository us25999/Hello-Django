
from django.urls import path, include

from .views import *



urlpatterns = [
    path('roles', showRoles, name="showRoles"),
]