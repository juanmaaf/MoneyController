# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Estandarización**: ¿La herramienta promueve una estructura estándar y organizada para la definición de tareas, ayudando a mantener un código limpio y reutilizable?  
- **Mantenimiento y comunidad**: ¿La herramienta tiene soporte activo, actualizaciones regulares y una comunidad que pueda responder dudas?  

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas populares: Invoke, Make, Task y Just. Además, se considerará la opción de gestionar las tareas mediante scripts de Python. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke)  
   - **Estandarización**: Proporciona flexibilidad, pero no sigue una estructura predefinida.  
   - **Mantenimiento y comunidad**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Estandarización**: Utiliza un formato estándar `Makefile` que fomenta claridad y organización en proyectos pequeños y medianos.  
   - **Mantenimiento y comunidad**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia.    

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   - **Estandarización**: La estructura YAML promueve una organización clara y legible, adecuada para proyectos de cualquier tamaño.  
   - **Mantenimiento y comunidad**: Es un proyecto activo, con soporte continuo y compatible con múltiples plataformas, lo que asegura un buen mantenimiento futuro, y tiene una cmunidad en continuo crecimiento.   

4. **Just**: 
   [Just](https://github.com/casey/just)   
   - **Estandarización**: Proporciona una sintaxis clara y organizada a través de `Justfile`.  
   - **Mantenimiento y comunidad**: Es un proyecto activo y bien mantenido, con actualizaciones regulares y una comunidad creciente.  

5. **Gestión de tareas con scripts de Python**:   
   - **Estandarización**: No impone ninguna estructura, lo que puede generar desorden.  
   - **Mantenimiento y comunidad**: Dependen de la versión de Python instalada en el entorno y de las habilidades del desarrollador.     
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en este proyecto, destacándose por su formato estándar `Makefile`. Éste promueve organización y claridad, ideal para proyectos estructurados. Aunque herramientas como Just y Task ofrecen sintaxis modernas, requieren configuraciones adicionales que pueden no ser adecuadas para un proyecto minimalista como el que se desarrolla en este repositorio. Invoke y los scripts en Python, aunque flexibles, carecen de estandarización, lo que dificulta el mantenimiento. Make ofrece la solución más práctica y directa para las necesidades del proyecto.   