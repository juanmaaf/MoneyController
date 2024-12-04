# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Archivo de configuración específico**: La herramienta debe centralizar la configuración de las tareas en un único archivo específico.  
- **Mantenimiento y comunidad**: La herramienta debe tener soporte activo, actualizaciones regulares y una comunidad activa que pueda responder dudas. Podemos comprobar este criterio en la página de Snyk Advisor de cada herramienta o en la página de GitHub viendo el número de PR, issues y las últimas versiones disponibles. 

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas populares: Invoke, Make, Task y Just. Además, se considerará la opción de gestionar las tareas mediante scripts de Python. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke) 
   [Invoke Snyk](https://snyk.io/advisor/python/invoke) 
   - **Archivo de configuración**: No utiliza un archivo específico. Usa scripts de Python.
   - **Mantenimiento y comunidad**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Archivo de configuración**: Utiliza el archivo `Makefile`.  
   - **Mantenimiento y comunidad**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia.    

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   - **Archivo de configuración**: Utiliza la estructura YAML en el archivo `taskfile.yaml`. 
   - **Mantenimiento y comunidad**: Es un proyecto activo, con soporte continuo y compatible con múltiples plataformas, lo que asegura un buen mantenimiento futuro, y tiene una comunidad en continuo crecimiento.   

4. **Just**: 
   [Just](https://github.com/casey/just)   
   - **Archivo de configuración**: Utiliza el archivo`Justfile`.  
   - **Mantenimiento y comunidad**: Es un proyecto activo y bien mantenido, con actualizaciones regulares y una comunidad creciente.  

5. **Gestión de tareas con scripts de Python**:   
   - **Archivo de configuración**: No utiliza un archivo específico. Usa scripts de Python.  
   - **Mantenimiento y comunidad**: Dependen de la versión de Python instalada en el entorno y de las habilidades del desarrollador.     
   
## Conclusión

De todas las herramientas comparadas, descarto inicialmente Invoke y los Scripts de Python, dado que, aunque son bastante flexibles, carecen de un archivo de configuración específico. Además, Invoke tiene un mantenimiento inactivo, como podemos ver en la página de Snyk Advisor. 

El resto de herramietas (Make, Task y Just) son bastante similares y cumplen los criterios, ya que tienen un archivo de configuración específico y son proyectos activos, con un mantenimiento contínuo y comunidades grandes y en crecimiento. **Make** es la que tiene mayor comunidad al haberte establecido y mantenido por muchos años. Por lo tanto, es la opción más adecuada para gestionar las tareas del proyecto que se desarrolla en este repositorio.    