from rest_framework.routers import DefaultRouter #lo importante es que viene con api root
from .api import UserViewSet, UserViewGenericViewSet #agregamos esto
from .routers import CustomRouter


user_router = DefaultRouter()

user_custom_router = CustomRouter()

user_router.register(r'users', UserViewSet, basename="users")
user_custom_router.register(r'custom/users', UserViewGenericViewSet, basename="users_custom")

urlpatterns = user_router.urls