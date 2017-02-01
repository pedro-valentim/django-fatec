from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home, cadastro

urlpatterns = [
    url(r'^inicio/', home, name='home'),
    url(r'^cadastro/', cadastro, name='cadastro'),
    url(r'^administracao/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
