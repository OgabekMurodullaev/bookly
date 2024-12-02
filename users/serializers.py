from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password")

    def create(self, validated_data):
        user = User.objects.filter(username=validated_data.get("username"))
        if user.exists():
            raise serializers.ValidationError({"username": "A user with that username already exists."})

        user = User.objects.create(username=validated_data.get("username"), email=validated_data.get("email"),
                                   phone_number=validated_data.get("phone_number"))
        user.set_password(validated_data.get("password"))
        user.save()
        return user


