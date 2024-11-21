# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con `pyproject.toml`**: Debe integrarse adecuadamente con el archivo `pyproject.toml` para una configuración unificada dentro del ecosistema Python. Es un requisito mínimo.  
- **Automatización de tareas personalizada**: Debe permitir la definición y automatización de tareas específicas, como pruebas y verificación de estilo de código, además de gestionar dependencias entre tareas.   
- **Proyectos simples**: La herramienta debe estar preparada para gestionar proyectos simples, dado que el problema que se resuelve en este repositorio es bastante simple.  

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cinco herramientas populares: Invoke, Make, Nox, Tox y Fabric. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   - **Automatización**: Permite la automatización de tareas personalizadas de manera flexible usando Python. Ideal para tareas como pruebas, verificación de estilo, y más.  
   - **Adaptación a proyectos simples**: Aunque es poderoso, requiere cierta configuración inicial y programación en Python, lo que puede ser excesivo para tareas básicas. 

2. **Make**: 
   - **Automatización**: Muy flexible y potente, ideal para proyectos con tareas complejas y dependencias. Utiliza una sintaxis simple y clara para definir las reglas de ejecución.  
   - **Adaptación a proyectos simples**: Es ideal para tareas básicas y no requiere configuraciones avanzadas ni dependencias externas.  

3. **Tox**: 
   - **Automatización**: Enfocado en la automatización de pruebas en múltiples entornos. Permite configurar pruebas en `pyproject.toml`, pero está especializado en testing.     
   - **Adaptación a proyectos simples**: Limitado para proyectos simples si no se necesita soporte para múltiples entornos de pruebas.  

4. **Nox**: 
   - **Automatización**: Similar a Tox, permite definir tareas personalizadas y pruebas con Python. Necesita un archivo de configuración separado.     
   - **Adaptación a proyectos simples**: Requiere más configuración inicial, pero es más flexible que Tox para tareas no relacionadas con testing.  

5. **Fabric**: 
   - **Automatización**: Ideal para ejecutar tareas de automatización remota, como despliegues y administración de servidores. Permite definir tareas en Python.  
   - **Adaptación a proyectos simples**: Está más orientado a tareas de administración remota, lo que lo hace innecesariamente complejo para tareas locales simples.  
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en proyectos simples, debido a su simplicidad, capacidad de automatización de tareas locales y mínima configuración. Aunque Tox y Nox ofrecen características avanzadas para testing, su enfoque y configuración adicional no son necesarias. Por otro lado, Fabric está diseñado para automatización remota, y por último Invoke requiere más configuración inicial, lo que lo hace excesivo para proyectos simples.  