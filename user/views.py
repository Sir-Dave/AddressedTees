from rest_framework import generics, permissions
from rest_framework.response import Response
from user.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from .models import Account


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.BasePermission]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "Successfully registered a new user"
            data["email"] = user.email
            data["first_name"] = user.first_name
            data["last_name"] = user.last_name
            data["token"] = Token.objects.get(user=user).key

        else:
            data = serializer.errors
        return Response(data)