from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("EcomApp.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('docs/', include_docs_urls(title ='EComerceAPI')),
    path(
        "schema",
        get_schema_view(
            title="EcomerceAPI", 
            description="API for Ecommerce…", 
            version="1.0.0"
        ),
        name="openapi-schema",
    ),
    # path('auth/', include('djoser.urls.jwt')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
