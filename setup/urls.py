from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DUVIDAS SOBRE A PARTE DE AUTENTICACAO CONSULTAR NO LINK ABAIXO
# https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
