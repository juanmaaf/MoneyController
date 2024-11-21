# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Compatibilidad con `pyproject.toml`**: Debe integrarse adecuadamente con el archivo `pyproject.toml` para una configuración unificada dentro del ecosistema Python. Es un requisito mínimo.  
- **Centralización de configuraciones**: La herramienta debe permitir definir todas las tareas en un solo archivo o estructura centralizada para facilitar la gestión y mantenimiento.  
- **Automatización de tareas personalizada**: Debe permitir la definición y automatización de tareas específicas, como pruebas y verificación de estilo de código, además de gestionar dependencias entre tareas.  
- **Proyectos simples**: La herramienta debe estar preparada para gestionar proyectos simples, dado que el problema que se resuelve en este repositorio es bastante simple.


## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares: Invoke, Make, y Pipenv. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   - **Centralización**: Las tareas se definen en un archivo Python (`tasks.py`), lo que facilita la organización y el mantenimiento.  
   - **Automatización**: Permite la automatización de tareas personalizadas de manera flexible usando Python. Ideal para tareas como pruebas, verificación de estilo, y más.  
   - **Adaptación a proyectos simples**: Aunque es poderoso, requiere cierta configuración inicial y programación en Python, lo que puede ser excesivo para tareas básicas. 

2. **Make**: 
   - **Centralización**: Utiliza el tradicional `Makefile` para definir tareas, lo que centraliza la configuración de las tareas. 
   - **Automatización**: Muy flexible y potente, ideal para proyectos con tareas complejas y dependencias. Utiliza una sintaxis simple y clara para definir las reglas de ejecución.  
   - **Adaptación a proyectos simples**: Es ideal para tareas básicas y no requiere configuraciones avanzadas ni dependencias externas.  

3. **Pipenv**: 
   - **Centralización**: No centraliza tareas automatizadas; se enfoca en la gestión de dependencias y entornos virtuales, pero no gestiona tareas personalizadas.      
   - **Automatización**: Limitada a ejecutar comandos simples como pipenv run, pero no está orientada a tareas complejas ni automatización personalizada.  
   - **Adaptación a proyectos simples**:  Adecuado para gestionar dependencias y entornos en proyectos pequeños, pero no cubre la automatización de tareas, lo que lo limita para este tipo de proyectos.   
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en proyectos simples, debido a su simplicidad, centralización de configuraciones y facilidad de integración con el ecosistema Python.  