# Gestor de Dependencias
En el desarrollo del anterior objetivo, se usó el archivo `pyproject.toml` como archivo de configuración del proyecto para poder seguir las buenas prácticas del lenguaje. Usar este archivo sigue las buenas prácticas del leguaje ya que desde las siguientes Propuestas de Mejora de Python (PEP) se llega al acuerdo de usarlo: [PEP 517](https://peps.python.org/pep-0517/) y el [PEP 518](https://peps.python.org/pep-0518/).

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta elegida como gestor de dependencias debe usar `pyproject.toml` como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.    
- **Rapidez operativa**: La herramienta debe ser lo más rápida posible para instalar dependencias de manera eficiente y con un impacto mínimo en el flujo de desarrollo.  
- **Mantenimiento y comunidad**: La herramienta debe tener soporte activo, actualizaciones regulares y una comunidad activa que pueda responder dudas. Podemos comprobar este criterio en la página de Snyk Advisor de cada herramienta.

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas: Poetry, PDM, Hatch y UV. La comparación se basa en los criterios específicos establecidos.  

1. **Poetry**: 
   [Poetry](https://github.com/python-poetry/poetry)    
   [Poetry Snyk](https://snyk.io/advisor/python/poetry)  
   - **Rapidez**: Aunque Poetry es rápido y eficiente, su enfoque en una gestión más completa puede implicar una ligera sobrecarga en comparación con herramientas más ligeras.  
   - **Mantenimiento y comunidad**: Tiene un desarrollo activo, con actualizaciones frecuentes y una comunidad amplia.   

2. **PDM**:  
   [PDM](https://github.com/pdm-project/pdm)   
   [PDM Snyk](https://snyk.io/advisor/python/pdm)     
   - **Rapidez**: PDM es rápido, pero puede ser más complejo debido al uso de PEP 582.  
   - **Mantenimiento y comunidad**: Cuenta con un mantenimiento activo y está ganando popularidad. La comunidad está en crecimiento, aunque es más pequeña que la de Poetry, al ser una herramienta más reciente.  

3. **Hatch**: 
   [Hatch](https://github.com/pypa/hatch)  
   [Hatch Snyk](https://snyk.io/advisor/python/hatch)  
   - **Rapidez**: Hatch es más lento que otras opciones especializadas en tareas más simples debido a su enfoque en proyectos más complejos y sus características avanzadas.  
   - **Mantenimiento y comunidad**: Cuenta con un mantenimiento activo y su comunidad es bastante pequeña.

4. **UV**: 
   [UV](https://github.com/astral-sh/uv)   
   [UV Snyk](https://snyk.io/advisor/python/uv)  
   - **Rapidez**: UV es extremadamente rápida, como se indica en la página de Snyk Advisor, tanto en la instalación de dependencias como en la inicialización de entornos. 
   - **Mantenimiento y comunidad**: Es relativamente nueva, con un mantenimiento activo pero una comunidad aún pequeña. 

## Conclusión

En primer lugar, descarto Hatch por ser el más lento al estar orientado a proyectos complejos. Entre Poetry, PDM y UV, herramientas compatibles con `pyproyect.toml`, rápidas y con mantenimiento activo, elijo finalmente **UV** ya que es el más rápido. Podemos justificar esta afirmación apoyándonos en los benckmarks que publica UV en su página de GitHUB, donde se compara con Poetry y PDM. [Benckmarks](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)  