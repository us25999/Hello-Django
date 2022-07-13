
from django.db import models


class  Roles(models.Model) :
    role_id = models.IntegerField(primary_key= True ,)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role



class  DrawerFields(models.Model) :
    field_id = models.IntegerField(primary_key= True , )
    field = models.CharField(max_length=100)
    field_link = models.URLField()
    role_id = models.ManyToManyField(Roles,related_name='drawerField', blank= True)

    def __str__(self):
        return self.field



class  Users(models.Model) :
    user_id = models.IntegerField(primary_key= True ,)
    user_name = models.CharField(max_length=100)  
    role_id = models.ForeignKey(Roles,related_name='user', blank=True, null= True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.user_name
        
