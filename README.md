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

## Generación de CSV de ratings
Ejecutar este comando en el directorio del proyecto
```
python manage.py ratings_csv <ruta_donde_quiero_crear_el_fichero.csv>
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