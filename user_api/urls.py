from user_api.views import logout_view, register_view
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
