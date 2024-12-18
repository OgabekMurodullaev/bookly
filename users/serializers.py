from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import User, Profile, Follow


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

    @extend_schema_field(int)
    def get_followers_count(self, obj):
        return obj.followers.count()

    @extend_schema_field(int)
    def get_following_count(self, obj):
        return obj.following.count()


class UserFollowSerializer(serializers.ModelSerializer):
    followed = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Profile
        fields = ["followed"]

    def create(self, validated_data):
        follower = self.context['request'].user.profile
        followed = validated_data['followed']

        if follower == followed:
            raise serializers.ValidationError("You cannot follow yourself")

        follow, created = Follow.objects.get_or_create(follower=follower, followed=followed)

        if not created:
            raise serializers.ValidationError("You are already following this user.")

        return follow


class UserUnfollowSerializer(serializers.ModelSerializer):
    followed = serializers.IntegerField()

    class Meta:
        model = Follow
        fields = ['followed']