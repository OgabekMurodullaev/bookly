from rest_framework import serializers

from .models import User, Profile


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "user_type")

class ProfileListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ("user", "profile_image")


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers = serializers.SerializerMethodField('get_followers_count')
    following = serializers.SerializerMethodField('get_following_count')

    class Meta:
        model = Profile
        fields = ("user", "profile_image", "followers", "following")

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
