from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class defined_views(models.Model):
    name = models.CharField(max_length=150)

class defined_permissions(models.Model):
    name = models.CharField(max_length=150)

class menuler(models.Model):
    adi= models.CharField(max_length=150, null=True)
    sira= models.PositiveIntegerField(null=True, blank=True)
    parentId= models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    viewId= models.ForeignKey(defined_views, null=True, on_delete=models.CASCADE)
    menu_type= models.CharField(max_length=150, null=True)

class user_menu_permission(models.Model):
    userId = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    menuID = models.ForeignKey(menuler, null=False, on_delete=models.CASCADE)
    permissionID = models.ForeignKey(defined_permissions, null=True, on_delete=models.CASCADE)
