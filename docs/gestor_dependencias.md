# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con el estándar `pyproject.toml`**: La herramienta debe usar pyproject.toml como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo.  
- **Proyectos simples**: La herramienta debe estar preparada para gestionar proyectos simples, dado que el problema que se resuelve en este repositorio es bastante simple.  
- **Uso y configuración sencillos**: La herramienta debe ser fácil de instalar, configurar y usar, sin requerir pasos complejos o una curva de aprendizaje elevada.    

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares que cumplen con los requisitos mínimos: Poetry, PDM, y Hatch. La comparación se basa en los criterios específicos establecidos.  

1. **Poetry**:  
   - **Adaptación a proyectos simples**: Ofrece un flujo de trabajo simple e intuitivo con comandos claros como poetry init para inicializar un proyecto y poetry add para agregar dependencias.  
   - **Facilidad de uso y configuración**: Es fácil de instalar y configurar, con una documentación clara y bien estructurada que facilita su integración rápida.  

2. **PDM**:  
   - **Adaptación a proyectos simples**: Ofrece un flujo de trabajo directo y sencillo, especialmente adecuado para quienes prefieren el estándar PEP 582, que instala dependencias localmente en lugar de usar entornos virtuales.  
   - **Facilidad de uso y configuración**:  Ofrece un flujo de trabajo directo, pero requiere cierta comprensión del modelo de PEP 582 y puede no ser tan bien visto para quienes buscan una configuración sencilla. 

3. **Hatch**: 
   - **Adaptación a proyectos simples**: Aunque es flexible y poderosa, Hatch tiene una curva de aprendizaje más pronunciada y está más orientada a proyectos con configuraciones complejas.   
   - **Facilidad de uso y configuración**: Su configuración inicial y uso pueden ser más complejos debido a su enfoque en proyectos más grandes y avanzados.  

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su facilidad de uso y su capacidad para adaptarse a proyectos simples, como el que se desarrolla en este repositorio.  