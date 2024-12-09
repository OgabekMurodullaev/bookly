from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import User, Profile
from .serializers import SignUpSerializer, ProfileListSerializer, ProfileDetailSerializer


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
