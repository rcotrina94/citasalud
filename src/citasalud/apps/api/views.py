# coding=utf-8
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import UsuarioSerializer


class CurrentUserView(APIView):
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
