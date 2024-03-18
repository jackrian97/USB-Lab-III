from django.db import models

class Zapato(models.Model):
    marca = models.CharField(max_length=100, default='DEFAULT VALUE') # para almcenar la marca del zapato
    modelo = models.CharField(max_length=100, default='DEFAULT VALUE') # para almacenar el modelo del zapato
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # para almacenar el precio del zapato
    talla = models.CharField(max_length=10, default='DEFAULT VALUE') # para almacenar la talla del zapato
    imagen = models.ImageField(upload_to='zapatos/') # para almacenar la imagen del zapato
    created_at = models.DateTimeField(auto_now_add=True) # para almacenar la fecha de creacion del zapato
    updated_at = models.DateTimeField(auto_now=True) # para almacenar la fecha de actualizacion del zapato

    class Meta:
        db_table = 'zapatos' # nombre de la tabla en la base de datos
