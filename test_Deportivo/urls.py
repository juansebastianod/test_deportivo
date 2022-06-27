"""test_Deportivo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from deporte.views import Robar, entrenador,anadir,registrarDeportista,listar,Puntos,edicion_Puntos,editar_Puntos,puntos_dos,edicion_tiros2,editar_Tiros_Dos,puntos_tres,edicion_tiros3,editar_Tiros_Tres,home,Salto_vertical,edicion_Salto,editar_Salto,Robar,edicion_Robos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('entrenador/', entrenador),
    path('anadir/', anadir),
    path('registrarDeportista/',registrarDeportista),
    path('listar/',listar),
    path('puntos/',Puntos),
    path('edicion/<int:id>',edicion_Puntos),
    path('editarResultados/',editar_Puntos),
    path('tiroDos/',puntos_dos),
    path('edicion2/<int:id>',edicion_tiros2),
    path('editarTirosDos/',editar_Tiros_Dos),
    path('tiroTres/',puntos_tres),
    path('edicion3/<int:id>',edicion_tiros3),
    path('editarTirosTres/',editar_Tiros_Tres),
    path('editarTirosTres/',editar_Tiros_Tres),
    path('salto/',Salto_vertical),
    path('edicion4/<int:id>',edicion_Salto),
    path('editarSalto/',editar_Salto),
    path('robo/',Robar),
    path('edicion5/<int:id>',edicion_Robos),
    path('editarRobos/',edicion_Robos),
    

   

    


    


    



   
    


]
