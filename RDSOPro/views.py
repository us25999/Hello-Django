from multiprocessing import AuthenticationError
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from RDSOPro.models import *
from RDSOPro.serializer import *
from django.db import connection, transaction

@api_view(['GET'])
def get_user_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            user = Users.objects.get(user_id = id)
            usersSerializer = UsersSerializer(user)
            return Response(usersSerializer.data)

        user = Users.objects.all()
        usersSerializer = UsersSerializer(user,many=True)
        return Response(usersSerializer.data)

@api_view(['POST'])
def post_user_api(request):
    user_id = request.data['user_id']
    user = Users.objects.get(user_id=user_id)
    if user is None:
        return AuthenticationError('User does not exist !!!')
    else:
        usersSerializer = UsersSerializer(user)
        return Response(usersSerializer.data)


@api_view(['GET'])
def complaint_registration(request):
    complaint = ComplaintRegistration.objects.filter(status_flag='P')
    complaintSerializer = ComplaintRegistrationSerializer(complaint,many=True)
    return Response(complaintSerializer.data)


@api_view(['GET'])
def role_drawer_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            user = Roles.objects.get(role_id = id)
            rolesSerializer = RolesSerializer(user)
            return Response(rolesSerializer.data)

        user = Roles.objects.all()
        rolesSerializer = RolesSerializer(user,many=True)
        return Response(rolesSerializer.data)


@api_view(['POST'])
def cursor_api(request):
    user_id = request.data['user_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'SELECT DISTINCT "RDSOPro_drawerfields".* FROM "RDSOPro_drawerfields" INNER JOIN "RDSOPro_roles_field_id" ON "RDSOPro_drawerfields".field_id = "RDSOPro_roles_field_id".drawerfields_id INNER JOIN "RDSOPro_roles" ON "RDSOPro_roles_field_id".roles_id = "RDSOPro_roles".role_id INNER JOIN "RDSOPro_users_role_id" ON "RDSOPro_roles".role_id = "RDSOPro_users_role_id".roles_id INNER JOIN "RDSOPro_users" ON "RDSOPro_users_role_id".users_id = "RDSOPro_users".user_id WHERE user_id = {user_id}')
    users = cursor.fetchall()
    return Response(users)


@api_view(['POST'])
def assign_user_role(request):
    user_id = request.data['user_id']
    role_id = request.data['role_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'INSERT INTO "RDSOPro_users_role_id" (users_id, roles_id) VALUES ({user_id}, {role_id});')
    return HttpResponse(f"Assigned role successfully")


@api_view(['POST'])
def remove_user_role(request):
    user_id = request.data['user_id']
    role_id = request.data['role_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'DELETE FROM "RDSOPro_users_role_id" WHERE users_id = {user_id} AND roles_id = {role_id};')
    return HttpResponse(f"Removed role successfully")


@api_view(['POST'])
def view_user_role(request):
    user_id = request.data['user_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'Select "RDSOPro_roles".role_id from "RDSOPro_roles" INNER JOIN "RDSOPro_users_role_id" ON "RDSOPro_roles".role_id = "RDSOPro_users_role_id".roles_id WHERE users_id = {user_id};')
    roles = cursor.fetchall()
    return Response(roles)


@api_view(['GET'])
def role(request):
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'SELECT role_name FROM complaint_role_master')
    roles = cursor.fetchall()
    return Response(roles)


@api_view(['GET'])
def directorate(request):
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'SELECT directorate_id FROM complaint_directorate')
    directorate = cursor.fetchall()
    return Response(directorate)


@api_view(['POST'])
def sub_directorate(request):
    directorate_id = request.data['directorate_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f"SELECT sub_dir_id,directorate_id FROM complaint_sub_directorate WHERE directorate_id = '{directorate_id}'")
    subDirectorate = cursor.fetchall()
    return Response(subDirectorate)



    


    


























#def RDSOModels(request):
#    rolesobj=Roles.objects.all()
#    usersobj=Users.objects.all()
#    drawerfieldobj=DrawerFields.objects.all()
#    roleserializer=RolesSerializer(rolesobj,many=True)
#    userserializer=UsersSerializer(usersobj,many=True)
#    drawerfieldserializer=DrawerFieldSerializer(drawerfieldobj,many=True)

#    return Response(roleserializer.data)
    

    
    
    #return Response({
    #    'Roles': roleserializer.data,
    #    'DrawerFields': drawerfieldserializer.data,
    #    'Users': userserializer.data,
    #    })
