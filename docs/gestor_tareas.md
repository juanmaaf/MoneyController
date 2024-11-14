# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones y he optado por **Poetry**. Esta elección se basa en varios criterios específicos necesarios para el proyecto:

- **Centralización de configuraciones**: El proyecto requiere que la configuración de tareas y scripts se centralice en un solo archivo, idealmente en `pyproject.toml`, para una administración más simple.  
- **Automatización de tareas personalizada**: Necesitamos una herramienta que permita definir y ejecutar tareas como pruebas y verificación de estilo de código sin necesidad de archivos adicionales.  
- **Eficiencia para proyectos Python**: La herramienta debe estar optimizada para proyectos Python, permitiendo la automatización sin dependencias adicionales.  

## Razones para elegir Poetry como gestor de tareas

- **Centralización en `pyproject.toml`**: `Poetry` permite definir configuraciones y scripts de automatización directamente en el archivo `pyproject.toml`, manteniendo una estructura de proyecto ordenada sin la necesidad de archivos adicionales como `Makefile`.
- **Automatización de tareas**: Poetry permite definir y ejecutar comandos personalizados de manera sencilla, como ejecutar pruebas (`poetry run pytest`) o verificar el estilo de código (`poetry run flake8`). Esto elimina la necesidad de herramientas adicionales como `Make` o `Invoke`.  
- **Eficiencia en proyectos Python**: Al estar diseñado específicamente para trabajar con proyectos Python, `Poetry` optimiza el flujo de trabajo sin la necesidad de depender de herramientas externas o configuraciones adicionales.  

## Comparación con otras herramientas

- **Make**: Aunque `Make` es una herramienta poderosa y flexible, no está diseñada específicamente para proyectos Python, lo que implica la necesidad de crear y mantener un archivo `Makefile` adicional. Con Poetry, todas las tareas pueden centralizarse directamente en `pyproject.toml`, simplificando el proceso.  

- **Invoke**: Aunque `Invoke` es otro gestor de tareas popular en Python, añade una dependencia adicional que no es necesaria cuando se utiliza Poetry. Poetry cubre todas las necesidades de automatización de tareas para este proyecto de manera eficiente y directa.  

## Conclusión

**Poetry** es la opción ideal para la automatización de tareas en este proyecto, ya que permite gestionar tareas y comandos sin necesidad de herramientas adicionales, mejorando la eficiencia del flujo de trabajo y centralizando la configuración en un único archivo.  