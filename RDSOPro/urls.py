
from django.urls import path
from . import views



urlpatterns = [
    path('get-user-api/<int:pk>', views.get_user_api, name="get_user_api"),
    path('complaint', views.complaint_registration, name="complaint_registration"),
    path('post-user-api', views.post_user_api, name="post_user_api"),
]