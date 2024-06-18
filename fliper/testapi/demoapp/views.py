from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Role
from demoapp.seralizer import RoleSerializer

class RoleCreateView(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            response_data = {
                "status": True,
                "content": {
                    "data": {
                        "id": role.id,
                        "name": role.name,
                        "created_at": role.created_at,
                        "updated_at": role.updated_at,
                    }
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
