# Caso 2 · Miembros de mesa

## Según la guía

1. Abrir https://consultaelectoral.onpe.gob.pe/inicio y verificar si eres miembro de mesa. La guía menciona RENIEC, pero su enlace pertenece a ONPE.
2. Si es miembro de mesa, registrar DNI, región, provincia, distrito y dirección del local de votación.
3. Descargar la lista en una hoja de Excel. Solo contiene esos cinco campos. Repetir el registro para agregar más miembros de mesa.

La consulta se realiza directamente en el portal oficial. La aplicación permite registrar y exportar lo consultado.

## Instalación y ejecución

Con Docker Desktop abierto, ejecutar en esta carpeta:

```powershell
docker compose up --build -d --remove-orphans
```

Abrir http://localhost:5001. El parámetro --remove-orphans retira el contenedor del navegador de la versión anterior. Los registros locales permanecen en data/consultas.sqlite3. Los antiguos registros No o Pendiente no se incluyen en la lista de miembros de mesa.

Para detener la aplicación: `docker compose down`.

## Construir las tres imágenes

```powershell
docker build -t practica-caso2:1.0 .
docker build -f Dockerfile.optimizado -t practica-caso2:1.1-alpine .
docker build -f Dockerfile.multistage -t practica-caso2:1.2-multistage .
docker images --filter "reference=practica-caso2:*"
```

Para probar una variante, detener Compose y ejecutar, por ejemplo:

```powershell
docker run --rm -p 127.0.0.1:5001:5000 --mount "type=bind,source=${PWD}/data,target=/app/data" practica-caso2:1.2-multistage
```

## URL del repositorio

[Gonnarch/PC1-Farfan](https://github.com/Gonnarch/PC1-Farfan)

## Conclusiones

La consulta oficial permite verificar la condición de miembro de mesa. Excel reúne los DNIs y locales de los miembros registrados. Los tres Dockerfiles permiten construir la aplicación con imagen base, optimizada y multietapa; sus tamaños se comparan después de construirlas.

