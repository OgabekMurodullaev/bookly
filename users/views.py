from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Profile, Follow
from .serializers import SignUpSerializer, ProfileListSerializer, ProfileDetailSerializer, UserFollowSerializer, \
    UserUnfollowSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class ProfileListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


class UserFollowAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserFollowSerializer

    def post(self, request):
        serializer = UserFollowSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Successfully follow the user"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserUnfollowSerializer

    def post(self, request):
        serializer = UserUnfollowSerializer(data=request.data)
        if serializer.is_valid():
            follower = self.request.user.profile
            followed = serializer.validated_data.get('followed')

            follows = Follow.objects.get(follower=follower, followed=followed)
            if not follows:
                return Response({"detail": "You don't following the user"}, status=status.HTTP_400_BAD_REQUEST)

            follows.delete()
            return Response({"detail": "Successfully unfollowed the user"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
