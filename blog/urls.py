@"
from django.contrib import admin
from django.urls import path, include  # ¡Agrega 'include'!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ¡Esta línea conecta tus URLs!
]
"@ | Out-File -FilePath .\TuPrimeraPagina\urls.py -Encoding utf8

# 3. Crea el archivo de URLs de la app blog
@"
from django.urls import path
from . import views

urlpatterns = [
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('', views.index, name='index'),  # Página principal
]
"@ | Out-File -FilePath .\blog\urls.py -Encoding utf8