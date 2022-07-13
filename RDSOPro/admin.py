from django.contrib import admin
from .models import DrawerFields
from .models import Roles
from .models import Users

admin.site.register(Roles)
admin.site.register(DrawerFields)
admin.site.register(Users)
