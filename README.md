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


