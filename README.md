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
despues creamos la aplicacion con el comando
```bash
python manage.py startapp zapatos_app
```