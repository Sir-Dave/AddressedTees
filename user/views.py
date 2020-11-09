from rest_framework.response import Response
from user.serializers import RegistrationSerializer
from rest_framework import generics
from .models import User


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Successfully registered a new user"
            data["email"] = account.email
            data["first_name"] = account.first_name
            data["last_name"] = account.last_name

        else:
            data = serializer.errors
        return Response(data)
