from rest_framework import serializers
from user.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        account = User(first_name=self.validated_data["first_name"],
                       last_name=self.validated_data["last_name"],
                       email=self.validated_data["email"],
                       )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        # Fix the bug here
        if password != password2:
            serializers.ValidationError({"password": "Passwords do not match"})

        account.set_password(password)
        account.save()
        return account
