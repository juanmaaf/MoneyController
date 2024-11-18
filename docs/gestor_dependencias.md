# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta debe usar pyproject.toml como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.  
- **Control de versiones reproducible**: La herramienta debe permitir el bloqueo de versiones mediante un archivo de “lock” (poetry.lock o similar), para garantizar la consistencia en las versiones de dependencias en distintos entornos y colaboradores. Este criterio sí permite diferenciar las herramientas, ya que cada una maneja el "locking" de dependencias de manera distinta.   
- **Gestión de entornos virtuales integrada**: La herramienta debe crear y gestionar entornos virtuales automáticamente para cada proyecto, sin necesidad de configuraciones o herramientas adicionales. Este criterio ayuda a diferenciar, ya que no todas las herramientas tienen esta funcionalidad.    

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares que cumplen con los requisitos mínimos: Poetry, PDM, y Hatch. La comparación se basa en los criterios específicos establecidos.

1. **Poetry**: 
   - **Control de versiones**: Utiliza `poetry.lock` para asegurar versiones consistentes.  
   - **Entornos virtuales**: Crea y gestiona entornos virtuales automáticamente para cada proyecto, lo que facilita un flujo de trabajo sin configuraciones adicionales.  

2. **PDM**: 
   - **Control de versiones**: Ofrece un archivo de bloqueo `pdm.lock`.  
   - **Entornos virtuales**: La gestión de entornos virtuales es opcional y se basa en PEP 582, lo que no proporciona un entorno dedicado en algunos casos.  

3. **Hatch**: 
   - **Control de versiones**: Usa `hatch.lock` para bloqueo de versiones.  
   - **Entornos virtuales**: Gestiona automáticamente entornos virtuales, similar a Poetry.  

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su eficaz sistema de bloqueo de versiones y su capacidad para gestionar entornos virtuales de manera integrada.  