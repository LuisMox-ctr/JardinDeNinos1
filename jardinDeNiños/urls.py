"""
URL configuration for jardinDeNiños project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from inicio import views
from registros import views as registros_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="principal"),
    path('tareas/',views.tareas, name="tareas1"),
    path('dudas/',registros_views.dudas, name="dudas"),
    #path('reconocimientos/',views.reconocimientos, name="reconocimientos"),
    path('tareas', registros_views.registros, name="tareas"),
    path("entregar/<int:tarea_id>/", registros_views.entregar_tarea, name="entregar_tarea"),
    path("reconocimientos/", registros_views.reconocimientos, name="reconocimientos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)