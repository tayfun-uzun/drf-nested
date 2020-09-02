from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
# from opak.modmain.serializers import UserSerializer, GroupSerializer
from opak.userAuth.ld import authanticate
from .serializers import UserSerializer

from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group


class ldene(APIView):
    
    def post(self, request):
        
        ka = request.data['ka']
        pa = request.data['pa']

        response = {}
        
        if authanticate(ka, pa):
            print('----------------------------------------------------')
            print(self.__class__.__name__)
            print('****************************************************')
            query_set = Group.objects.filter(user = request.user)
            i = 0
            for g in query_set:
                i+= 1
                print(str( i ) + ' - ' + g.name)
                prms = g.permissions.all()
                for p in prms:
                    print('   - ' +p.name)
            # for grup in request.user.groups:
            #     print(grup)
            #     print(' - ')
            
            response['username'] = ka
            response['hataKodu'] = 0
            response['hataMesaji'] = ''
            return Response(response)

        response['hataKodu'] = 1
        response['hataMesaji'] = 'kullanici adi veya parola doğru değil'
        return Response(response)



class userView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
        
