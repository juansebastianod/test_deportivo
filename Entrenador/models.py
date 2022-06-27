from django.db import models
from .choices import sexos

# Create your models here.
class Entrenador(models.Model):
    codigoEntrenador = models.CharField(primary_key=True, max_length=6)
    nombres=models.CharField(max_length=30,verbose_name='Nombre')
    apellido_paterno=models.CharField(max_length=30,verbose_name='Apellido Paterno')
    apellido_materno=models.CharField(max_length=30,verbose_name='Apellido Materno')
    edad=models.PositiveSmallIntegerField()
    

    def nombre_completo(self):
        return "{}  {}  {}".format(self.nombres,self.apellido_paterno,self.apellido_materno)

    def __str__(self) -> str:
        return self.nombre_completo()

    class Meta:
        verbose_name='Entrenador'
        verbose_name_plural='Entrenadores'
        db_table='entrenador'


class Deportista(models.Model):
    
   
    codigoDeportista = models.CharField(primary_key=True, max_length=12)
    codigoEntrenador=models.ForeignKey(Entrenador,null=True,blank=True,on_delete=models.CASCADE)
    nombres=models.CharField(max_length=30,verbose_name='Nombre')
    apellido_paterno=models.CharField(max_length=30,verbose_name='Apellido Paterno')
    apellido_materno=models.CharField(max_length=30,verbose_name='Apellido Materno')
    edad=models.PositiveSmallIntegerField()
    altura=models.PositiveSmallIntegerField()
    email=models.CharField(max_length=30,verbose_name='Email')
    


    def __str__(self) -> str:
        return self.codigoDeportista

    class Meta:
        verbose_name='Deportista'
        verbose_name_plural='Deportistas'
        db_table='deportista'

class Test_Puntos(models.Model):

    codigoDeportista=models.ForeignKey(Deportista, on_delete=models.CASCADE)
    partidos=models.PositiveSmallIntegerField()
    puntos=models.PositiveSmallIntegerField()
    puntos_por_partidos=models.PositiveSmallIntegerField()

    

class Test_Tiros_De_Dos(models.Model):

    codigoDeportista=models.ForeignKey(Deportista, on_delete=models.CASCADE)
    partidos=models.PositiveSmallIntegerField()
    tiros_dentro=models.PositiveSmallIntegerField()
    tiros_fallidos=models.PositiveSmallIntegerField()
    porcentaje_tiro_de_dos=models.PositiveSmallIntegerField()

class Test_Tiros_De_Tres(models.Model):

    codigoDeportista=models.ForeignKey(Deportista, on_delete=models.CASCADE)
    partidos=models.PositiveSmallIntegerField()
    tiros_tres=models.PositiveSmallIntegerField()
    tiros_fallidos=models.PositiveSmallIntegerField()
    porcentaje_tiro_de_tres=models.PositiveSmallIntegerField()

class Robos(models.Model):

    codigoDeportista=models.ForeignKey(Deportista, on_delete=models.CASCADE)
    partidos=models.PositiveSmallIntegerField()
    robos=models.PositiveSmallIntegerField()
    robos_por_partido=models.PositiveSmallIntegerField()

class Salto(models.Model):

    codigoDeportista=models.ForeignKey(Deportista, on_delete=models.CASCADE)
    Salto=models.PositiveSmallIntegerField()
    


