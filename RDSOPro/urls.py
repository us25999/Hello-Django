
from django.urls import path
from . import views



urlpatterns = [
    path('get-user-api/<int:pk>', views.get_user_api, name="get_user_api"),
    path('complaint', views.complaint_registration, name="complaint_registration"),
    path('post-user-api', views.post_user_api, name="post_user_api"),
    path('role-drawer-api', views.role_drawer_api, name="role_drawer_api"),
    path('role-drawer-api/<int:pk>', views.role_drawer_api, name="role_drawer_api"),
    path('cursor-api', views.cursor_api, name="cursor_api"),
    path('remove-role', views.remove_user_role, name="remove_user_role"),
    path('user-role', views.userRole, name="userRole"),
    path('role', views.role, name="role"),
    path('directorate', views.directorate, name="directorate"),
    path('sub-directorate', views.sub_directorate, name="sub_directorate"),
    path('assign', views.assign_user_role, name="assign_user_role"),
    path('remove', views.remove_user_role, name="remove_user_role"),
    path('trains', views.new_trains, name="trains"),
]