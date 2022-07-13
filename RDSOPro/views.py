from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from RDSOPro.models import Roles,Users,DrawerFields
from RDSOPro.serializer import RolesSerializer,UsersSerializer,DrawerFieldSerializer

@api_view(['GET'])
def RDSOModels(request):
    rolesobj=Roles.objects.all()
    usersobj=Users.objects.all()
    drawerfieldobj=DrawerFields.objects.all()
    roleserializer=RolesSerializer(rolesobj,many=True)
    userserializer=UsersSerializer(usersobj,many=True)
    drawerfieldserializer=DrawerFieldSerializer(drawerfieldobj,many=True)
    return Response({
        'Roles': roleserializer.data,
        'DrawerFields': drawerfieldserializer.data,
        'Users': userserializer.data,
        })
