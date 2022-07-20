from multiprocessing import AuthenticationError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from RDSOPro.models import *
from RDSOPro.serializer import *

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
