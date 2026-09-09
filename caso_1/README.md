# Caso 1

## Instalación y ejecución

Requiere Docker Desktop iniciado. Abre una terminal en esta carpeta y ejecuta:

```powershell
docker compose up --build -d
```

Abre http://localhost:5000. Para ver registros: `docker compose logs -f`. Para detenerlo: `docker compose down`.

## Las tres imágenes de la guía

```powershell
docker build -t practica-caso_1:1.0.0 .
docker build -f Dockerfile.optimizado -t practica-caso_1:1.1.0-alpine .
docker build -f Dockerfile.multistage -t practica-caso_1:1.2.0-alpine .
docker images --filter "reference=practica-caso_1:*"
docker history practica-caso_1:1.0.0
docker inspect practica-caso_1:1.0.0
docker tag practica-caso_1:1.0.0 practica-caso_1:latest
```

Para probar una variante, detén primero Compose y ejecuta, por ejemplo:

```powershell
docker run --rm -p 127.0.0.1:5000:5000 --mount "type=bind,source=${PWD}/downloads,target=/app/downloads" practica-caso_1:1.2.0-alpine
```

La imagen base usa Debian Slim. La optimizada utiliza Alpine y usuario no root. La multietapa instala dependencias por separado y las copia a la imagen final. Los tamaños deben medirse: no se garantizan las cifras ilustrativas de la guía.

## Datos persistentes

La carpeta `downloads` se vincula con `/app/downloads` dentro del contenedor. Se conserva al detener o recrear el servicio. No incluir datos personales o videos en Git.

## Repositorio

[Gonnarch/PC1-Farfan](https://github.com/Gonnarch/PC1-Farfan)

## Uso

Pega un enlace de YouTube, Instagram, TikTok, Facebook o LinkedIn y pulsa Descargar video. La biblioteca permite reproducirlo o guardarlo mediante el navegador. El soporte real depende de yt-dlp y de las restricciones de cada plataforma; videos privados, autenticación o bloqueos pueden impedir la descarga. No se incorpora evasión de controles ni inicio de sesión.

`DOWNLOAD_DIR` en app.py define el directorio absoluto. La opción `outtmpl` define el nombre. Con Docker es `/app/downloads`; con Compose también aparece en `caso_1/downloads` en Windows. Guardar en mi equipo utiliza la ubicación configurada en el navegador. Las tres imágenes incluyen FFmpeg. La reproducción depende del códec compatible con el navegador.

La descarga es síncrona; espera a que termine antes de enviar otra. No se han probado descargas reales desde las cinco redes.

