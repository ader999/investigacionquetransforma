"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path ,include
from mi_proyecto import views
from blog.views import blog_app
from django.conf import settings
from django.conf.urls.static import static


#app_name = 'mi_proyecto'
#from .views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Vista para la ruta principal '/'
    path('acerca_de/',views.acerca_de,name='acerca_de'),
    path('contacto/',views.contacto,name="contacto"),
    path('login/', views.login, name='login'),
    path('notas/', views.notas, name='notas'),
    path('admin/',admin.site.urls),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
    path('blog/', include('blog.urls', namespace='blog'),),
    path('blog/', blog_app,name='blog_app'),


    #path('redirigir_a_blog/', views.redirigir_a_blog, name='redirigir_a_blog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)