# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Centralización de configuraciones**: La herramienta debe permitir definir todas las tareas en un solo archivo o estructura centralizada para facilitar la gestión y mantenimiento.  
- **Automatización de tareas personalizada**: Debe permitir la definición y automatización de tareas específicas, como pruebas y verificación de estilo de código, además de gestionar dependencias entre tareas.  
- **Compatibilidad con `pyproject.toml`**: Debe integrarse adecuadamente con el archivo `pyproject.toml` para una configuración unificada dentro del ecosistema Python.  

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares: Invoke, Make, y Pipenv. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   - **Centralización**: Las tareas se definen en un archivo Python (`tasks.py`), lo que facilita la organización y el mantenimiento.  
   - **Automatización**: Permite la automatización de tareas personalizadas de manera flexible usando Python. Ideal para tareas como pruebas, verificación de estilo, y más.
   - **Compatibilidad con `pyproject.toml`**: No tiene integración directa con pyproject.toml, pero se puede usar junto con otras herramientas de automatización, como `tox`.   

2. **Make**: 
   - **Centralización**: Utiliza el tradicional `Makefile` para definir tareas, lo que centraliza la configuración de las tareas. 
   - **Automatización**: Muy flexible y potente, ideal para proyectos con tareas complejas y dependencias. Utiliza una sintaxis simple y clara para definir las reglas de ejecución.
   - **Compatibilidad con `pyproject.toml`**: No es nativa de Python, pero se puede integrar bien en proyectos Python. Es común usarla junto con otras herramientas de Python como `tox` para gestionar tareas automatizadas y pruebas.

3. **Pipenv**: 
   - **Centralización**: Gestiona dependencias y entornos a través de `pyproject.toml`.  
   - **Automatización**: Limitada a ejecutar comandos simples como pipenv run, pero no está orientada a tareas complejas ni automatización personalizada.  
   - **Compatibilidad con `pyproject.toml`**: Totalmente compatible para la gestión de dependencias y entornos virtuales, pero no es adecuada para la automatización de tareas.  

## Conclusión

**Make** es la opción recomendada, ya que, aunque no es específica para Python, es flexible, compatible con `pyproject.toml` y permite una integración sencilla con otras herramientas de Python como `tox`.