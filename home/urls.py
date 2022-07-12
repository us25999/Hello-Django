
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('post-todo/', post_todo, name="post_todo"),
    path('get-todo/',get_todo, name="get_todo")
]