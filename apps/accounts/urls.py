from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, WebLoginView, SignUpView, ProfileView, HomeRedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home-redirect'),

    # Web auth/profile
    path('login/', WebLoginView.as_view(), name='web-login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

    #
    path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]