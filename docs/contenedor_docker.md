# Elección de imagen para contenedor Docker  

En el desarrollo de este objetivo, en primer lugar es necesario elegir una imagen para el contenedor. Para la búsqueda de las ímagenes me he basado principalmente en la página [DockerHub](https://hub.docker.com/). Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la imagen que mejor se ajusta a los objetivos del proyecto.  

## Criterios de Selección  

1. Se considerará que el tamaño de la imagen sea mínimo.    
2. Se considerará que la imagen esté bien mantenida y actualizada. Podremos verificar este criterio de forma objetiva basándonos en la página [DockerHub](https://hub.docker.com/) de cada imagen.  
3. Se considerará que el repositorio de la imagen ofrezca la versión de Python más actualizada. Se entiende por esta versión a la que ofrece cuando se instala Python como paquete `python3`. Este proyecto requiere una versión de Python superior a la 3.13.0, especificado en [Pyproject.toml](/pyproject.toml).          
4. Se considerará que la imagen ofrezca el SO más actualizado.  

## Comparación de Imágenes   

1. **Alpine Linux**:    
    [DockerHub](https://hub.docker.com/_/alpine)    
    Como podemos ver en su página de DockerHub, la imagen Alpine Linux está bien mantenida y actualizada, con una última versión publicada hace 6 días. El espacio de almacenamiento que ocupa son únicamente 5MB, 3.47 MB como archivo comprimido. No incluye las funcionalidades necesarias para el desarrollo de este proyecto (Python, UV, make). Instalando Python como paquete `python3`, su repositorio ofrece la versión 3.12.8.  

2. **Debian**:  
    [DockerHUB](https://hub.docker.com/_/debian)    
    Como podemos ver en su página de DockerHub, la imagen Debian está bien mantenida y actualizada, con una última versión publicada hace menos de un día. El espacio de almacenamiento que ocupa depende de la variante:    
        - [debian:latest](https://hub.docker.com/layers/library/debian/latest/images/sha256-7f8ed5d106371f33b3eac043c9cba5ac3cbd30c8a82896cc71ea00574b19157e). Como archivo comprimido, ocupa 46.23 MB. No incluye Python ni UV. Instalando Python como paquete `python3`, su repositorio ofrece la versión 3.11.2. SO Debian 12.                 
        - [debian:bullseye-slim](https://hub.docker.com/layers/library/debian/bullseye-slim/images/sha256-a20489c8fd4878b97c42bc09321c1d6a9475231bcb2779682d03f25677a383ab). Como archivo comprimido, ocupa 28.85 MB. No incluye Python ni Make ni UV. Instalando Python como paquete `python3`, su repositorio ofrece la versión 3.9.2. SO Debian 11.             
        - [debian:bookworm-slim](https://hub.docker.com/layers/library/debian/bookworm-slim/images/sha256-44831da5de1fbbfb71eab0b0c2dc99ceb03b0b889490fcc7beff6fcd7b6efc44). Como archivo comprimido, ocupa 26.91 MB. No incluye Python ni Make ni UV. Instalando Python como paquete `python3`, su repositorio ofrece la versión 3.11.2. SO Debian 12.         

3. **Python**:    
    [DockerHub](https://hub.docker.com/_/python)    
    Como podemos ver en su página de DockerHub, la imagen oficial de Python está bien mantenida y actualizada, con una última versión publicada hace menos de un día. El espacio de almacenamiento que ocupa depende de la variante:            
        - [python:slim-bullseye](https://hub.docker.com/layers/library/python/slim-bullseye/images/sha256-05eda5508b86b91a1058eb8d2e8d008d301939006f779476de2bc49e19f9d336). Como archivo comprimido, ocupa 41.84 MB. No incluye Make ni UV. Su repositorio incluye Python y ofrece la versión 3.13.1, ya que se descarga de forma manual descargando y compilando el código de Python de su página web empleando la variable de entorno `ENV PYTHON_VERSION 3.13.1`. SO Debian 11.           
        - [python:slim-bookworm](https://hub.docker.com/layers/library/python/slim-bookworm/images/sha256-13ae6b865089eade069cd3cf8156564e5e1c59332c407517bd8ebd27ab2ee723). Como archivo comprimido, ocupa 42.26 MB. No incluye Make ni UV. Su repositorio incluye Python y ofrece la versión 3.13.1, ya que se descarga de forma manual descargando y compilando el código de Python de su página web empleando la variable de entorno `ENV PYTHON_VERSION 3.13.1`. SO Debian 12.        

4. **Bitnami/python**:    
    [DockerHub](https://hub.docker.com/r/bitnami/python)    
    Cono podemos ver en su página de DockerHub, la imagen bitnami/python está bien mantenida y actualizada, con una última versión publicada hace 3 días. El espacio de almacenamiento que ocupa es 200.9 MB como archivo comprimido. No incluye Make ni UV. Su repositorio incluye Python y ofrece la versión 3.13.1.       

## Conclusión  

Después de comparar las imágenes, llega el momento de elegir una de ellas. Sin embargo, no podemos comparar los pesos de las imágenes cuando no incluyen las mismas funcionalidases. Por tanto, voy a comparar el peso de las imágenes una vez tienen instaladas las funcionalidades necesarias (UV, Make, Python). De las imágenes anteriores se compararán:   
    - Alpine Linux    
    - debian:bookworm-slim. Elijo la que tiene menos peso de las 3 variantes planteadas.      
    - python:slim-bookworm. A pesar de no ser la que tiene el menor peso como archivo comprimido de las 2 planteadas, es la que ofrece el SO más actualizado (Debian 12).       
    - bitnami/python    

Creando imágenes docker con las anteriores 4 bases mencionadas, incluyendo las funcionalidades necesarias para el desarrollo del proyecto, el resultado ha sido el siguiente. [Imagen](/docs/espacio_contenedores.png)  

Como podemos ver `python:slim-bookworm` y `debian:bookworm-slim` son las imágenes con menor peso y tienen un peso similar, 187 y 184 MB, respectivamente. Para decidir entre python:slim-bookworm y debian:bookworm-slim debemos atender a la versión de Pyhton que proporcionan. La primera proporciona la versión 3.13.1, última versión de Pyhton. La segunda proporciona la versión 3.11.2, bastante antigua. Por tanto, descartamos debian:bookworm-slim. ¿Cuál sería el peso de la imagen instalado Python de forma manual descargando la misma versión (3.13.1)? He creado una imagen con debian:bookworm instalando la versión 3.13.1 de forma manual en lugar de intalando el paquete `python3`. [Dockerfile Debian Python 3.13.1](/pruebas_contenedores/Dockerfile_debian_Python_3.13.1). Para instalar Python, me he basado en la instalación que hace la imagen `python:slim-bookworm` que podemos ver en [Dockerfile python:slim-bookworm](https://github.com/docker-library/python/blob/master/3.13/slim-bullseye/Dockerfile). 

Espacio que ocupa la nueva imagen [Almacenamiento Debian Python 3.13.1](/pruebas_contenedores/espacio_debian_python.png).  
Como podemos ver, el tamaño es considerablemente grande. La imagen `python:slim-bookworm` instala Pyhton de la misma forma y optimiza bastante la imagen hasta obtener los 187MB de espacio mencionados en el párrafo anterior. Si añadiese la parte que optimiza la imagen eliminando el contenido innecesario [Optimización](/pruebas_contenedores/Dockerfile_parte_optimizacion) obtendría la misma imagen `python:slim-bookworm`. No es viable hacer un Dockerfile desde 0 para nuestra herramienta partiendo de la imagen `debian:bookworm-slim` si se puede disponer de una imagen base ya optimizada y construida.  

Por tanto, elijo **python:slim-bookworm** como imagen base para el contenedor docker que se va a desarrollar en este proyecto.    