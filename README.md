# USB-Lab-III
CRUD using Django 
mi proyecto sera basado en un modelo de zapatos

# priemr paso configuracion de entorno
Creo el ambiente de desarrollo y para crear el ambiente del proyecto, ejecuto el siguiente comando en la terminal:

```bash
python -m venv zapatos_env
```

Este comando creará un nuevo entorno virtual de Python llamado `zapatos_env`.

Ahora necesitamos instalar Django, para ello puedes usar pip3 ejecutando el siguiente comando en la terminal:

```bash
pip3 install django
```

Esto instalará la última versión estable de Django en tu entorno Python puedes verificar su intalacion con el comando.

```bash
pip3 list   
```
ahora creamos el proyecto con el comando, asegurate de no estar en el entorno virtual. deberia estar al mismo nivel que el entorno virtual.
```bash
django-admin startproject zapatos_proyecto
```
deberia de crear una carpeta con el nobre ´zapatos_proyecto´ y dentro de ella deberia de haber un archivo llamado ´manage.py´

despues creamos la aplicación y para ello nos ubicamos en la carpeta del proyecto y ejecutamos el siguiente comando:
```bash
python manage.py startapp zapatos_app
```
registro la aplicación en el archivo `settings.py` del proyecto, en la lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...    
    'zapatos_app',

]
```

por ultimo hacemo la coneccion a la base de datos instalando el paquete psycopg2 con el comando:
```bash
pip3 install psycopg2-binary==2.9.5
```

# segundo paso configuracion de la base de datos

Para este proyecto usaremos fl0 para la base de datos asi que, en el archivo `settings.py` del proyecto, en el diccionario `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'lab1',#nombre de la base de datos
        'USER' : 'fl0user', #usuario de la base de datos
        'PASSWORD' : '******', #contraseña de la base de datos
        'HOST' : 'ep-dark-bread-a55zy6yw.us-east-2.aws.neon.fl0.io', #host de la base de datos
        'PORT' : '5432', #si lo dejas vacío tomara el puerto por default
    }
}
```

En el archivo `models.py` de la aplicación, creamos el modelo `Zapato`:

```python
from django.db import models

class Zapato(models.Model):
    marca = models.CharField(max_length=100, default='DEFAULT VALUE')#para almcenar la marca del zapato
    modelo = models.CharField(max_length=100, default='DEFAULT VALUE')#para almacenar el modelo del zapato
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)#para almacenar el precio del zapato
    talla = models.CharField(max_length=10, default='DEFAULT VALUE')#para almacenar la talla del zapato
    imagen = models.ImageField(upload_to='zapatos/')#para almacenar la imagen del zapato
    created_at = models.DateTimeField(auto_now_add=True)#para almacenar la fecha de creacion del zapato
    updated_at = models.DateTimeField(auto_now=True)#para almacenar la fecha de actualizacion del zapato

    class Meta:
        db_table = 'zapatos' #nombre de la tabla en la base de datos
´´´
