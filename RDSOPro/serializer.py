from rest_framework import serializers
from RDSOPro.models import DrawerFields
from RDSOPro.models import Users
from RDSOPro.models import Roles


class DrawerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawerFields
        fields = "__all__"

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"  