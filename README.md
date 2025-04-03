# TrabajoDjango
1. Crea un entorno virtual y actívalo:
python -m venv venv
venv\Scripts\activate

2. Instala las dependencias:
pip install asgiref==3.8.1
pip install Django==5.2
pip install djangorestframework==3.16.0
pip install sqlparse==0.5.3
pip install tzdata==2025.2

3. Aplica las migraciones de la base de datos:
python manage.py migrate

4.Crea un superusuario
 python manage.py createsuperuser

5. Ejecuta el servidor de desarrollo:
python manage.py runserver

7. Abre el navegador y accede a http://127.0.0.1:8000/
