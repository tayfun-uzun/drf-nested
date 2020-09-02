from django.contrib.auth.models import User, Group
from .models import (
                        defined_permissions, defined_views, menuler, user_menu_permission
                    )

from rest_framework import serializers



class defined_permissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = defined_permissions
        fields = ['id', 'name'] 

class defined_viewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = defined_views
        fields = ['id', 'name'] 

class menulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = menuler
        # fields = ['id',  'adi', 'sira', 'parentId', 'viewId', 'menu_type'] 
        fields = ['adi'] 

class user_menu_permissionSerializer(serializers.ModelSerializer):
    menu = menulerSerializer(many=True)
    class Meta:
        model = user_menu_permission
        fields = ['menuID', 'permissionID', 'menu'] 

class UserSerializer(serializers.ModelSerializer):
    menuler = user_menu_permissionSerializer(
        source='user_menu_permission_set', many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'menuler']