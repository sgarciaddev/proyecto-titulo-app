# Proyecto de título - App (docker)

<div align="center">

[![docker-badge]][docker-web] [![nginx-badge]][nginx-web]

</div>

Archivos y configuraciones de Docker para generar contenedores para la
aplicación.

## Uso

La aplicación se compone de 3 contenedores (frontend, backend y un proxy con
NGINX), los que trabajan en conjunto gracias a Docker Compose. Para levantar
los contenedores, se debe ejecutar el siguiente comando:

```bash
docker compose up
```

Para detener los contenedores, se debe ejecutar el siguiente comando:

```bash
docker compose down
```

<!-- badges -->

[docker-badge]: https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=FFF&style=flat

[docker-web]: https://www.docker.com/

[nginx-badge]: https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=FFF&style=flat

[nginx-web]: https://www.nginx.com/

