from django.urls import path, include, re_path
from django.views.generic import TemplateView
# from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
