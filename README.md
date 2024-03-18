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
    'zapatos_app',
    ...
]
```

