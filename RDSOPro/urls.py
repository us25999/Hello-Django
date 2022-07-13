
from django.urls import path, include

from .views import *



urlpatterns = [
    path('models', RDSOModels, name="RDSOModels"),
]