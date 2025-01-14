# Elección de imagen para contenedor Docker

En el desarrollo de este objetivo, en primer lugar es necesario elegir una imagen para el contenedor. Para la búsqueda de las ímagenes me he basado principalmente en la página [DockerHub](https://hub.docker.com/). Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la imagen que mejor se ajusta a los objetivos del proyecto.

## Criterios de Selección

1. Se considerará que el tamaño de la imagen sea mínimo.  
2. Se considerará que la imagen esté bien mantenida y actualizada. Podremos verificar este criterio de forma objetiva basándonos en la página [DockerHub](https://hub.docker.com/) de cada imagen.  

## Comparación de Herramientas

1. **Alpine Linux**:  
    [DockerHub](https://hub.docker.com/_/alpine)  
    Como podemos ver en su página de DockerHub, la imagen Alpine Linux está bien mantenida y actualizada, con una última versión publicada hace 6 días. El espacio de almacenamiento que ocupa son únicamente 5MB, 3.47 MB como archivo comprimido. No incluye las funcionalidades necesarias para el desarrollo de este proyecto (Python, UV, make).

2. **Debian**:  
    [DockerHUB](https://hub.docker.com/_/debian)  
    Como podemos ver en su página de DockerHub, la imagen Debian está bien mantenida y actualizada, con una última versión publicada hace menos de un día. El espacio de almacenamiento que ocupa depende de la variante:  
        - [debian:latest](https://hub.docker.com/layers/library/debian/latest/images/sha256-7f8ed5d106371f33b3eac043c9cba5ac3cbd30c8a82896cc71ea00574b19157e). Como archivo comprimido, ocupa 46.23 MB. No incluye Python ni UV.     
        - [debian:bullseye-slim](https://hub.docker.com/layers/library/debian/bullseye-slim/images/sha256-a20489c8fd4878b97c42bc09321c1d6a9475231bcb2779682d03f25677a383ab). Como archivo comprimido, ocupa 28.85 MB. No incluye Python ni Make ni UV.  
        - [debian:bookworm-slim](https://hub.docker.com/layers/library/debian/bookworm-slim/images/sha256-44831da5de1fbbfb71eab0b0c2dc99ceb03b0b889490fcc7beff6fcd7b6efc44). Como archivo comprimido, ocupa 26.91 MB. No incluye Python ni Make ni UV.  

3. **Python**:  
    [DockerHub](https://hub.docker.com/_/python)  
    Como podemos ver en su página de DockerHub, la imagen oficial de Python está bien mantenida y actualizada, con una última versión publicada hace menos de un día. El espacio de almacenamiento que ocupa depende de la variante:  
        - [python:slim](https://hub.docker.com/layers/library/python/slim/images/sha256-13ae6b865089eade069cd3cf8156564e5e1c59332c407517bd8ebd27ab2ee723). Como archivo comprimido, ocupa 42.26 MB. No incluye Make ni UV.    
        - [python:slim-bullseye](https://hub.docker.com/layers/library/python/slim-bullseye/images/sha256-05eda5508b86b91a1058eb8d2e8d008d301939006f779476de2bc49e19f9d336). Como archivo comprimido, ocupa 41.84 MB. No incluye Make ni UV.   
        - [python:slim-bookworm](https://hub.docker.com/layers/library/python/slim-bookworm/images/sha256-13ae6b865089eade069cd3cf8156564e5e1c59332c407517bd8ebd27ab2ee723). Como archivo comprimido, ocupa 42.26 MB. No incluye Make ni UV.  

4. **Bitnami/python**:  
    [DockerHub](https://hub.docker.com/r/bitnami/python)  
    Cono podemos ver en su página de DockerHub, la imagen bitnami/python está bien mantenida y actualizada, con una última versión publicada hace 3 días. El espacio de almacenamiento que ocupa es 200.9 MB como archivo comprimido. No incluye Make ni UV. 

## Conclusión

Después de comparar las imágenes, llega el momento de elegir una de ellas. Sin embargo, no podemos comparar los pesos de las imágenes cuando no incluyen las mismas funcionalidases. Por tanto, voy a comparar el peso de las imágenes una vez tienen instaladas las funcionalidades necesarias (UV, Make, Python). De las imágenes anteriores se compararán:  
    - Alpine Linux  
    - debian:bookworm-slim. Elijo la que tiene menos peso de las 3 variantes planteadas.    
    - python:slim-bullseye. Elijo la que tiene menos peso de las 3 variantes planteadas.    
    - bitnami/python  

