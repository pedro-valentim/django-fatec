from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home, cadastro, login, logout

urlpatterns = [
    url(r'^inicio/', home, name='home'),
    url(r'^cadastro/', cadastro, name='cadastro'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^administracao/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
