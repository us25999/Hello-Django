from multiprocessing import AuthenticationError
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['POST','GET'])
def complaint_registration(request):
    if request.method == 'POST':
        status_flag = request.data['status_flag']
        complaint = ComplaintRegistration.objects.filter(status_flag=status_flag)
        complaintSerializer = ComplaintRegistrationSerializer(complaint,many=True)
        return Response(complaintSerializer.data)

    elif request.method == 'GET' :
        complaint = ComplaintRegistration.objects.filter(escalated='Y')
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
@api_view(['GET'])
def userRole(request):
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f"SELECT user_id, role_name, directorate_id, sub_dir_id FROM complaint_user_role INNER JOIN complaint_role_master ON complaint_role_master.role_id = complaint_user_role.role_id  WHERE status IS NULL;")
    userRoles = cursor.fetchall()
    return Response(userRoles)
@api_view(['POST'])
def remove_user_role(request):
    user_id = request.data['user_id']
    role_name = request.data['role_name']
    dir_id = request.data['dir_id']
    subDir_id = request.data['subDir_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f"UPDATE complaint_user_role SET status = 'D' WHERE user_id='{user_id}' AND role_id=(SELECT role_id FROM complaint_role_master WHERE role_name='{role_name}') AND directorate_id='{dir_id}' AND sub_dir_id='{subDir_id}';")
    return Response(f'Role is removed successfuly... Refresh to view the changes.')


@api_view(['POST'])
def assign_user_role(request):
    user_id = request.data['user_id']
    role_name = request.data['role_name']
    dir_id = request.data['dir_id']
    subDir_id = request.data['subDir_id']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f"SELECT * FROM comm_app_login_master WHERE ipasid = '{user_id}'  OR aadhar_no = '{user_id}';")
    if cursor.rowcount == 0:
        return Response(f"Can't assign...!!! User does not exist.")
    else:
        cursor.execute(f"SELECT * FROM comm_app_login_master WHERE (ipasid = '{user_id}' OR aadhar_no='{user_id}') AND emp_status='w' AND status='v' AND active_flag= 'y';")
        if cursor.rowcount == 0:
            return Response(f"Can't assign...!!! User is not verified.")
        else:
            cursor.execute(f"SELECT status FROM complaint_user_role WHERE user_id='{user_id}' AND role_id=(SELECT role_id FROM complaint_role_master WHERE role_name='{role_name}') AND directorate_id='{dir_id}' AND sub_dir_id='{subDir_id}';")
            if cursor.rowcount == 0:
                cursor.execute(f"INSERT INTO complaint_user_role (user_id, role_id, directorate_id, sub_dir_id, entry_on) VALUES ('{user_id}',(SELECT role_id FROM complaint_role_master WHERE role_name='{role_name}'),'{dir_id}','{subDir_id}',NOW());")
                return Response(f'Role is successfully assigned...')
            else:
                status = cursor.fetchone()[0]
                if status == 'D':
                    cursor.execute(f"INSERT INTO complaint_user_role (user_id, role_id, directorate_id, sub_dir_id,entry_on) VALUES ('{user_id}',(SELECT role_id FROM complaint_role_master WHERE role_name='{role_name}'),'{dir_id}','{subDir_id}',NOW());")
                    return Response(f'Role is assigned successfully...')
                else:
                    return Response(f"Can't assign...!!! Specified role is already assigned.")



            

    





@api_view(['GET'])
def role(request):
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f'SELECT DISTINCT role_name FROM complaint_role_master ORDER BY role_name ASC')
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
    cursor.execute(f"SELECT sub_dir_id FROM complaint_sub_directorate WHERE directorate_id = '{directorate_id}'")
    subDirectorate = cursor.fetchall()
    return Response(subDirectorate)




@api_view(['POST'])
def new_trains(request):
    source = request.data['source']
    destination = request.data['destination']
    if connection.connection is None:
        cursor=connection.cursor()
    cursor=connection.connection.cursor()
    cursor.execute(f"SELECT * FROM newtrains WHERE source = '{source}' AND destination = '{destination}'")
    trains = cursor.fetchall()
    return Response(trains)
                    

    




