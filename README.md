# Práctica calificada 1 · Laboratorio 04

Basada en GLAB-S04-JFARFAN-2026-02.docx.

- caso_1/: aplicación para descargar videos de las redes indicadas en la guía.
- caso_2/: acceso al portal oficial para consultar la condición de miembro de mesa y registro de DNI, región, provincia, distrito y dirección del local en Excel.

Cada carpeta incluye Dockerfile, Dockerfile.optimizado, Dockerfile.multistage y README con instalación y ejecución. Caso 1 usa http://localhost:5000 y caso 2 http://localhost:5001.

## Instalación y ejecución

Requisitos: Docker Desktop instalado y en ejecución. Descargar o clonar este repositorio y abrir una terminal en la carpeta raíz del proyecto.

Para iniciar el caso 1:

```powershell
cd caso_1
docker compose up --build -d
```

Abrir http://localhost:5000, pegar el enlace de un video y descargarlo. Los archivos se guardan en caso_1/downloads mediante el montaje configurado.

Para iniciar el caso 2 desde la misma terminal:

```powershell
cd ..\caso_2
docker compose up --build -d
```

Abrir http://localhost:5001. Consultar la condición de miembro de mesa en el enlace oficial. Si corresponde, registrar DNI, región, provincia, distrito y dirección del local, guardar y descargar la lista en Excel.

Para detener cada aplicación, ejecutar `docker compose down` dentro de la carpeta del caso correspondiente. Los README de cada caso incluyen los comandos para construir las imágenes base, optimizada y multietapa.

## URL del repositorio

[Gonnarch/PC1-Farfan](https://github.com/Gonnarch/PC1-Farfan)

## Conclusiones

1. Cada aplicación se empaqueta con su código y dependencias mediante un Dockerfile, y puede ejecutarse de forma independiente en un contenedor.
2. La versión optimizada utiliza Alpine y un usuario sin privilegios de administrador. La versión multietapa separa la instalación de dependencias de la imagen final. La diferencia de tamaño se determina comparando las imágenes construidas.
3. En el caso 1, FFmpeg permite unir audio y video cuando la descarga los obtiene por separado. El montaje de la carpeta downloads conserva los archivos fuera del contenedor.
4. En el caso 2, la consulta se realiza en el portal oficial indicado por la guía. La aplicación reúne en Excel el DNI, la ubicación y la dirección del local de las personas registradas como miembros de mesa.

