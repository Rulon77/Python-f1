# Blog F1

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
# Superusuario de pruebas
username:Admin
contraseña:Admin

# Dentro de la Web sin login
+ Se podra ver lista de pilos, biografia, lista de escuderias, calendario y "Sobre mi"
+ Busqueda de pilotos y escuderias
+ Completar formulario para creacion de usuario registrado

# Dentro de la Web con login
+ Los mismos permisos del usuario no logeado
+ Se podra crear pilotos y escuderias completando el formulario
+ Edicion de pilotos y escuderias
+ Cargar un avatar a eleccion 

# Dentro del Admin
+ Los mismo permisos que el usuario logeado
+ Crear pilotos y poder cargar una foto del mismo

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```




