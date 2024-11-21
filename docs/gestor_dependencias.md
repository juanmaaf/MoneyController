# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta debe usar pyproject.toml como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.  
- **Bloqueo de versiones**: La herramienta debe generar un archivo `.lock`, para garantizar que desarrolladores en distintos entornos usen las mismas versiones de las dependencias. 
- **Proyectos simples**: La herramienta debe estar preparada para gestionar proyectos simples, dado que el problema que se resuelve en este repositorio es bastante simple.

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares que cumplen con los requisitos mínimos: Poetry, PDM, y Hatch. La comparación se basa en los criterios específicos establecidos.

1. **Poetry**:  
   - **BLoqueo de versiones**: Genera un archivo `poetry.lock`, que garantiza la reproducibilidad en diferentes entornos.   
   - **Adaptación a proyectos simples**: Ofrece un flujo de trabajo simple e intuitivo con comandos claros como poetry init para inicializar un proyecto y poetry add para agregar dependencias.   

2. **PDM**: 
   - **Bloqueo de versiones**: Genera un archivo `pdm.lock`, lo que asegura consistencia en las dependencias.  
   - **Adaptación a proyectos simples**: Ofrece un flujo de trabajo directo y sencillo, especialmente adecuado para quienes prefieren el estándar PEP 582, que instala dependencias localmente en lugar de usar entornos virtuales.  

3. **Hatch**: 
   - **Bloqueo de versiones**:  Genera un archivo de bloqueo `hatch.lock`, asegurando la reproducibilidad.  
   - **Adaptación a proyectos simples**: Aunque es flexible y poderosa, Hatch tiene una curva de aprendizaje más pronunciada y está más orientada a proyectos con configuraciones complejas.  

4. **Flit**:
   - **Bloqueo de versiones**:  No genera un archivo de bloqueo de versiones, lo que es una desventaja significativa respecto a las otras herramientas analizadas.   
   - **Adaptación a proyectos simples**: Es extremadamente sencillo y rápido de usar, pero su principal enfoque está en la publicación de paquetes en lugar de la gestión de múltiples dependencias en un proyecto.   

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su eficaz sistema de bloqueo de versiones y su capacidad para adaptarse a proyectos simples, como el que se desarrolla en este repositorio.  