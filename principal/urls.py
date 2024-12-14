"""
URL configuration for principal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio, name='inicio'),
    path('registro/',views.Registro, name='registro'),
    path('ingresar/',views.Ingresar, name='ingresar'),
    path('salir/',views.Salir, name='salir'),
    path('tareas/',views.Tareas, name='tareas'),
    path('tareas/crear/',views.CrearTarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/',views.ActualizarTarea, name='actualizar_tarea'),
    path('tareas/<int:tarea_id>/completar/',views.CompletarTarea, name='completar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/',views.EliminarTarea, name='eliminar_tarea'),
]
