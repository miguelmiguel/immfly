# immfly

## Repositorio.

El proyecto se encuentra guardado en el siguiente repositorio
```
https://github.com/miguelmiguel/immfly
```
Descargue el proyecto en un directorio local.

## Despliegue

Para desplegarlo, se puede hacer con docker-compose, en el directorio donde se descargó
```
docker-compose build
docker-compose up
```

En el primer despliegue, puede que se requiera volver a desplegar, ya que al levantar el servicio
de mysql y no existir todavía la base de datos, intenta desplegar el backend en una base de datos que
no existe. 

La aplicación se despliega en `http://localhost:8989`

Si ya se desplegó el proyecto y está levantada la base de datos, también se puede desplegar el servidor 
de django con el `manage.py runserver` indicando que utilice el local_settings.

```
python manage.py runserver --settings=immfly.local_settings
```

## Ejecutar tests
Para poder ejecutar tests, se debe acceder a la shell del mysql para dar permisos al usuario creado
para poder crear la base de datos para tests.

```
docker exec -it immfly-mysql sh
mysql -p  
<datos usuario, contraseña y contraseña de root en el docker-compose.yml>

GRANT ALL PRIVILEGES ON *.* TO 'immfly_user'@'%';
FLUSH PRIVILEGES;
```

Después, se pueden ejecutar tanto desde la shell del contenedor del backend, como desde el local, usando los settings locales.

Desde el contenedor:
```
docker exec -it immfly-mysql sh
cd backend
python manage.py tests
```

o desde el directorio local:
```
python manage.py tests --settings=immfly.local_settings
```

## Generación de CSV de ratings
Ejecutar este comando en el directorio del proyecto.

Desde el contenedor:
```
python manage.py ratings_csv <ruta_donde_quiero_crear_el_fichero.csv>
```

o desde el directorio local:
```
python manage.py ratings_csv <ruta_donde_quiero_crear_el_fichero.csv>  --settings=immfly.local_settings
```

## Endpoints
Se utilizó DRF para crear el API REST para los modelos.
Se crearon endpoints para los contenidos y canales. Son los siguientes:

### Listado de Contents
```
http://localhost:8989/content/
```
Aquí se puede crear nuevos contents.

### Detalles de un Content
```
http://localhost:8989/content/<id>
```
Aquí se puede editar el content en particular o borrarlo

### Listado de Channels
```
http://localhost:8989/channel/
```
Aquí se puede crear nuevos channels.

### Detalles de un Channel
```
http://localhost:8989/channel/<id>
```
Aquí se puede editar el channel en particular o borrarlo

### Listado de Subchannels de un Channel
```
http://localhost:8989/channel/<id>/subchannels
```
### Listado de Contents de un Channel
```
http://localhost:8989/channel/<id>/contents
```

**PD.:** Si se despliega la app con `manage.py` desde local, los puertos cambian a `8000` o al que se 
indique en el despliegue.