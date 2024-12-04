# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Estructura Centralizada**: ¿La herramienta promueve una estructura en un archivo específico para definir las tareas?   
- **Mantenimiento y comunidad**: ¿La herramienta tiene soporte activo, actualizaciones regulares y una comunidad que pueda responder dudas?  

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas populares: Invoke, Make, Task y Just. Además, se considerará la opción de gestionar las tareas mediante scripts de Python. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke)  
   - **Estructura**: No utiliza un archivo específico. Usa un script de Python.
   - **Mantenimiento y comunidad**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Estructura**: Utiliza el archivo `Makefile`.  
   - **Mantenimiento y comunidad**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia.    

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   - **Estructura**: Utiliza la estructura YAML en el archivo `taskfile.yaml`. 
   - **Mantenimiento y comunidad**: Es un proyecto activo, con soporte continuo y compatible con múltiples plataformas, lo que asegura un buen mantenimiento futuro, y tiene una cmunidad en continuo crecimiento.   

4. **Just**: 
   [Just](https://github.com/casey/just)   
   - **Estructura**: Utiliza el archivo`Justfile`.  
   - **Mantenimiento y comunidad**: Es un proyecto activo y bien mantenido, con actualizaciones regulares y una comunidad creciente.  

5. **Gestión de tareas con scripts de Python**:   
   - **Estructura**: No utiliza un archivo específico. Usa un script de Python.  
   - **Mantenimiento y comunidad**: Dependen de la versión de Python instalada en el entorno y de las habilidades del desarrollador.     
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en este proyecto, destacándose por su estructura centralizada en el archivo `Makefile`. Éste promueve organización y claridad, ideal para proyectos estructurados. Aunque herramientas como Just y Task también ofrecen archivos específicos, son más modernas requieren configuraciones adicionales que pueden no ser adecuadas para un proyecto minimalista como el que se desarrolla en este repositorio. Invoke y los scripts en Python, aunque flexibles, carecen de archivo de configuración específico. Make ofrece la solución más práctica y directa para las necesidades del proyecto.   