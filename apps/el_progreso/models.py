from django.db import models

class Entrenador (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    especialidad = models.CharField(max_length=100)

    def __init__(self):
        return f"{self.nombre} {self.apellido}"

class Actividad (models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __init__(self):
        return f"{self.nombre} {self.tipo}"

class Espacio (models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad_personas = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __init__(self):
        return f"{self.nombre} {self.tipo}"

class Evento (models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

    def __init__(self):
        return self.nombre


class Socio (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    numero_socio = models.IntegerField()

    def __init__(self):
        return f"{self.nombre} {self.apellido}"

