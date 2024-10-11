from django.contrib import admin
from rest_framework import permissions
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Menew API",
        default_version='v1',
        description="Menew Api swagger",
        terms_of_service="https://github.com/menew-be/menew-django-test",
        contact=openapi.Contact(email="amir@sefati.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('estimate/', include('estimate.urls')),
    path('user/', include('user.urls')),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh')

]
