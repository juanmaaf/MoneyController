# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta debe usar pyproject.toml como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.  
- **Uso y configuración sencillos**: La herramienta debe ser fácil de configurar y usar, sin requerir pasos complejos o una curva de aprendizaje elevada. 
- **Rapidez operativa**: La herramienta debe ser lo más rápida posible para instalar dependencias de manera eficiente y con un impacto mínimo en el flujo de desarrollo.      

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas: Poetry, PDM, Hatch y UV. La comparación se basa en los criterios específicos establecidos.  

1. **Poetry**: 
   [Poetry](https://github.com/python-poetry/poetry)  
   - **Facilidad de uso y configuración**: Es fácil de instalar y configurar, con una documentación clara y bien estructurada que facilita su integración rápida.  
   - **Rapidez**: Aunque Poetry es rápido y eficiente, su enfoque en una gestión más completa puede implicar una ligera sobrecarga en comparación con herramientas más ligeras.  

2. **PDM**:  
   [PDM](https://github.com/pdm-project/pdm)    
   - **Facilidad de uso y configuración**:  Ofrece un flujo de trabajo directo, pero requiere cierta comprensión del modelo de PEP 582, por lo que no es tan fácil de configurar.   
   - **Rapidez**: PDM es rápido, pero puede ser más complejo debido al uso de PEP 582.  

3. **Hatch**: 
   [Hatch](https://github.com/pypa/hatch)  
   - **Facilidad de uso y configuración**: Su configuración inicial y uso pueden ser más complejos debido a su enfoque en proyectos más grandes y avanzados. 
   - **Rapidez**: Hatch es más lento que otras opciones especializadas en tareas más simples debido a su enfoque en proyectos más complejos y sus características avanzadas.  

4. **UV**: 
   [UV](https://github.com/astral-sh/uv)  
   - **Facilidad de uso y configuración**: UV tiene una instalación rápida y sencilla, sin la necesidad de configuraciones complejas.   
   - **Rapidez**: UV es extremadamente rápida, tanto en la instalación de dependencias como en la inicialización de entornos.  

## Conclusión

**UV** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su facilidad de uso, su alta velocidad y su capacidad para adaptarse a proyectos simples, como el que se desarrolla en este repositorio.  