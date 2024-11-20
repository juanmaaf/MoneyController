# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta debe usar pyproject.toml como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.  
- **Gestión de entornos virtuales integrada**: La herramienta debe crear y gestionar entornos virtuales automáticamente para cada proyecto, sin necesidad de configuraciones o herramientas adicionales. Este criterio ayuda a diferenciar, ya que no todas las herramientas tienen esta funcionalidad.    
- **Eficiencia y simplicidad**: La herramienta debe estar preparada para gestionar proyectos simples, dado que el problema que se resuelve en este repositorio es bastante simple. Además, debe ser eficiente. 

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares que cumplen con los requisitos mínimos: Poetry, PDM, y Hatch. La comparación se basa en los criterios específicos establecidos.

1. **Poetry**:  
   - **Entornos virtuales**: Crea y gestiona entornos virtuales automáticamente para cada proyecto, lo que facilita un flujo de trabajo sin configuraciones adicionales.  
   - **Eficiencia y simplicidad**: La herramienta es bastante eficiente, ya que tiene una instalación y gestión de dependencias muy optimizada. Además, está adaptada para proyectos de cualquier tamaño. 

2. **PDM**: 
   - **Entornos virtuales**: La gestión de entornos virtuales es opcional y se basa en PEP 582, lo que no proporciona un entorno dedicado en algunos casos.  
   - **Eficiencia y simplicidad**: La herramienta es bastante eficiente y simple en proyectos pequeños al basarse en PEP 582.

3. **Hatch**: 
   - **Entornos virtuales**: Gestiona automáticamente entornos virtuales, similar a Poetry.  
   - **Eficiencia y simplicidad**: La herramienta es bastante eficiente, pero es adecuada para proyectos con avanzada configuración.

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su eficaz sistema de bloqueo de versiones y su capacidad para gestionar entornos virtuales de manera integrada.  