
from django.urls import path
from . import views



urlpatterns = [
    path('get-user-api/<int:pk>', views.get_user_api, name="get_user_api"),
    path('complaint', views.complaint_registration, name="complaint_registration"),
    path('post-user-api', views.post_user_api, name="post_user_api"),
    path('role-drawer-api', views.role_drawer_api, name="role_drawer_api"),
    path('role-drawer-api/<int:pk>', views.role_drawer_api, name="role_drawer_api"),
    path('cursor-api', views.cursor_api, name="cursor_api"),
]