"""todoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

#from tasks.urls import router

schema_view = get_schema_view(
    openapi.Info(
        title="Todo Api",
        default_version="v1",
        description="API de lista de tareas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="msfm@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[AllowAny]
)
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r"api/", include("tasks_viewset.urls")),
    #path("api/v1/", include(router.urls)),
    path(r"api/v1/", include("tasks.urls")),
    path(r"api/v1/", include("users.urls")),
    path(r"api-auth/", include("authapp.urls")),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
