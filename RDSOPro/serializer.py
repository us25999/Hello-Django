from pyexpat import model
from rest_framework import serializers
from RDSOPro.models import *



class DrawerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawerFields
        fields = "__all__"

class RolesSerializer(serializers.ModelSerializer):
    field_id = DrawerFieldSerializer(many=True)
    class Meta:
        model = Roles
        fields = ['role_id','role','field_id']

class UsersSerializer(serializers.ModelSerializer):
    role_id = RolesSerializer(many=True)
    class Meta:
        model = Users
        fields = ['user_id','user_name','role_id']  

