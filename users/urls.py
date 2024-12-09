from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import SignUpView, ProfileListAPIView, ProfileDetailAPIView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profiles/', ProfileListAPIView.as_view(), name='profiles'),
    path('<int:id>/profile/', ProfileDetailAPIView.as_view(), name='profile'),
]