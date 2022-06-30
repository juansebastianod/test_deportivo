from copy import deepcopy
import re
from django.shortcuts import render,redirect
from .models import Deportista, Salto, Test_Puntos, Test_Tiros_De_Dos, Test_Tiros_De_Tres,Robos

# Create your views here.

def entrenador(request):
    return render(request,'entrenador.html')

def home(request):
    return render(request,'index.html')

def anadir(request):

     return render(request,'anadir.html')
     
def listar(request):

     deportista=Deportista.objects.all()
     return render(request,'listado.html',{"deportista":deportista})

def registrarDeportista(request):

    codigo=request.POST['txtCodigo']                            
    nombres = request.POST['txtNombre']
    Apellido_paterno=request.POST['txtApellido_Paterno']
    Apellido_Materno=request.POST['txtApellido_Materno']
    edad=request.POST['numEdad'] 
    altura=request.POST['numAltura'] 
    
    email=request.POST['numEmail'] 

    deportista = Deportista.objects.create(
    codigoDeportista=codigo, nombres=nombres,apellido_paterno=Apellido_paterno,
    apellido_materno=Apellido_Materno,edad=edad,altura=altura,email=email)

    
    deportistas=Deportista.objects.all()
    b=0
    for a in deportistas:

        if(codigo==a.codigoDeportista):
            puntos=Test_Puntos.objects.create(codigoDeportista=a,partidos=0,puntos=0,
            puntos_por_partidos=0)
            dos=Test_Tiros_De_Dos.objects.create( codigoDeportista=a,partidos=0,tiros_dentro=0, tiros_fallidos=0,
            porcentaje_tiro_de_dos=0)
            tres=Test_Tiros_De_Tres.objects.create(codigoDeportista=a,partidos=0,tiros_tres=0, tiros_fallidos=0,
            porcentaje_tiro_de_tres=0)

            robar=Robos.objects.create(codigoDeportista=a,partidos=0,robos=0,robos_por_partido=0)

            saltar=Salto.objects.create(codigoDeportista=a,Salto=0)
            
            break

    return render(request,'entrenador.html')

def Puntos(request):

    punto=Test_Puntos.objects.all()
    return render(request,'Puntos.html',{"Punto":punto})

def edicion_Puntos(request,id):
     Puntos = Test_Puntos.objects.get(id=id)
     data={
        'titulo':'Edicion de Puntos',
         'Puntos':Puntos

     }

     return render(request,'edicion.html',data)

def editar_Puntos(request):

    id=int(request.POST['txtid'])
    
    puntos = request.POST['numPuntos']
    
    
    puntos =int(puntos)
    
    resultados = Test_Puntos.objects.get(id=id)
    resultados.partidos=resultados.partidos+1  
    resultados.puntos=resultados.puntos+puntos
    puntos_por_patido=resultados.puntos/resultados.partidos
    resultados.puntos_por_partidos=puntos_por_patido

    resultados.save()
    
    return render(request,'registro.html')

def puntos_dos(request):

    puntoDos=Test_Tiros_De_Dos.objects.all()

    
    return render(request,'tirosDos.html',{"Tiros":puntoDos})

def edicion_tiros2(request,id):
     tiros=Test_Tiros_De_Dos.objects.get(id=id)
     data={
        'titulo':'Edicion tiros de dos ',
         'tiros':tiros
     }

     return render(request,'edicion2.html',data)

def editar_Tiros_Dos(request):
    id = request.POST.get('txtId', False)
    
    tiros = request.POST['numTiros']
    fallidos=request.POST['numFallidos']
    tiros =int(tiros)
    fallidos =int(fallidos)
    resultados=Test_Tiros_De_Dos.objects.get(id=id)
    resultados.partidos=resultados.partidos+1  
    resultados.tiros_dentro= resultados.tiros_dentro+tiros
    resultados.tiros_fallidos= resultados.tiros_fallidos+fallidos
    tiros_dos=(resultados.tiros_fallidos*100)/resultados.tiros_dentro
    t=100-tiros_dos
    resultados.porcentaje_tiro_de_dos=t

    resultados.save()
    
    return render(request,'registro2.html')


def puntos_tres(request):

    puntoTres=Test_Tiros_De_Tres.objects.all()
    return render(request,'tirosTres.html',{"Tiros":puntoTres})

def edicion_tiros3(request,id):
     tiros=Test_Tiros_De_Tres.objects.get(id=id)
     data={
        'titulo':'Edicion tiros de dos ',
         'tiros':tiros
     }

     return render(request,'edicion3.html',data)

def editar_Tiros_Tres(request):
    id = request.POST.get('txtId', False)
    
    tiros = request.POST['numTres']
    fallidos=request.POST['numFallidosTres']
    tiros =int(tiros)
    fallidos =int(fallidos)
    resultados=Test_Tiros_De_Tres.objects.get(id=id)
    resultados.partidos=resultados.partidos+1  
    resultados.tiros_tres= resultados.tiros_tres+tiros
    resultados.tiros_fallidos= resultados.tiros_fallidos+fallidos
    tiros_dos=(resultados.tiros_fallidos*100)/resultados.tiros_tres
    t=100-tiros_dos
    resultados.porcentaje_tiro_de_tres=t

    resultados.save()
    
    return render(request,'registro3.html')

def Salto_vertical(request):
    salto=Salto.objects.all()
    return render(request,'saltos.html',{"salto":salto})

def edicion_Salto(request,id):
     tiros=Salto.objects.get(id=id)
     data={
        'titulo':'Edicion tiros de dos ',
         'tiros':tiros
     }

     return render(request,'edicion4.html',data)

def editar_Salto(request):
    id = request.POST.get('txtId', False)
    
    
    salto=request.POST['numSalto']
    
    resultados=Salto.objects.get(id=id)
   
    resultados.Salto=salto

    resultados.save()
    
    return render(request,'registro.html')

def Robar(request):

    punto=  Robos.objects.all()
    return render(request,'robos.html',{"Robos":punto})

def edicion_Robos(request,id):
     robo=Robos.objects.get(id=id)
     data={
        'titulo':'Edicion tiros de dos ',
         'Robos':robo
     }

     return render(request,'edicion5.html',data)

def editar_Robos(request):

    id = request.POST.get('txtId', False)

    
    
    robo = request.POST['numRobos']
    
    
    robo =int(robo)
    
    resultados = Robos.objects.get(id=id)
    resultados.partidos=resultados.partidos+1  
    resultados.robos=resultados.robos+robo
    robos_por_partidos=resultados.robos/resultados.partidos
    resultados.robos_por_partido=robos_por_partidos

    resultados.save()
    
    return render(request,'registro.html')
