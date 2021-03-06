"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from apps.accounts.views import CustomRegisterView, CustomLogoutView, CustomLoginView, VerifyToken
from apps.author.views import AuthorViewset
from apps.category.views import CategoryViewset
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

router = routers.SimpleRouter()
router.register('categories', CategoryViewset)
router.register('authors', AuthorViewset)


schema_view = get_schema_view(
   openapi.Info(
      title="biblioteca API",
      default_version='v1',
      description="Documentação de apis da bilbioteca",
      terms_of_service="",
      contact=openapi.Contact(email="felipe.alves2014@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   permission_classes=(permissions.IsAuthenticated,),
   public=False,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/',  CustomLoginView.as_view(), name='login'),
    path('account/logout/', CustomLogoutView.as_view(), name='logout'),
    path('account/registration/', CustomRegisterView.as_view(), name='register'),
    path('account/verify/', VerifyToken.as_view(), name='verify-token'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
