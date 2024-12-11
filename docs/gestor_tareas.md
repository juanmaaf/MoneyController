# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Espacio de almacenamiento**: La herramienta debe un peso en espacio de almacenamieto bajo para no aumentar el espacio necesario en la máquina para el desarrollo del proyecto. Podemos comprobar este criterio en la página de GitHub de cada herramienta indicando comprobando el peso de la versión más reciente.   
- **Mantenimiento y comunidad**: La herramienta debe tener soporte activo, actualizaciones regulares y una comunidad activa que pueda responder dudas. Podemos comprobar este criterio en la página de Snyk Advisor de cada herramienta o en la página de GitHub viendo el número de PR, issues y las últimas versiones disponibles. 

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas populares: Invoke, Make, Task y Just. Además, se considerará la opción de gestionar las tareas mediante scripts de Python. La comparación se basa en los criterios específicos establecidos.  

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke) 
   [Invoke Snyk](https://snyk.io/advisor/python/invoke) 
   - **Espacio de almacenamiento**: La última versión disponible (2.2.0) pesa 1,2MB. Además, depende de scripts de Python, con tamaño variable en función del número de tareas.  
   - **Mantenimiento y comunidad**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Espacio de almacenamiento**: La última versión disponible (4.4.1) pesa 3,5MB. Viene preinstalada en máquinas Ubuntu como la que desarrolla este proyecto. 
   - **Mantenimiento y comunidad**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia.    

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   - **Espacio de almacenamiento**: La última versión disponible (3.40.0) pesa entre 5 y 6 MB según la máquina.  
   - **Mantenimiento y comunidad**: Es un proyecto activo, con soporte continuo y compatible con múltiples plataformas, lo que asegura un buen mantenimiento futuro, y tiene una comunidad en continuo crecimiento.   

4. **Just**: 
   [Just](https://github.com/casey/just)   
   - **Espacio de almacenamiento**: La última versión disponible (1.37.0) pesa 1,7MB. 
   - **Mantenimiento y comunidad**: Es un proyecto activo y bien mantenido, con actualizaciones regulares y una comunidad creciente.  

5. **Gestión de tareas con scripts de Python**:   
   - **Espacio de almacenamiento**: No tiene un tamaño definido. Al igual que el script que usa Invoke para gestionar las tareas, dependerá del número de tareas. 
   - **Mantenimiento y comunidad**: Dependen de la versión de Python instalada en el entorno y de las habilidades del desarrollador.     
   
## Conclusión

De todas las herramientas comparadas, descarto inicialmente Invoke, ya que es la que tiene un mantenimiento inactivo como bien podemos ven en su página de Snyk Advisor. En segundo lugar, descarto Task, ya que es la más pesada de todas, y los Scripts de Python, ya que no tienen un tamaño definido como el resto de herramientas. 

Finalmente, entre Make y Just, dado que desarrollo el proyecto en una máquina Ubuntu donde Make viene preinstalado y no ocasiona espacio adicional, elijo **Make** como gestor de tareas del proyecto que se desarrolla en este repositorio. En caso de desarrollar este proyecto en una máquina con otro sistema operativo, donde Make no estuviese preinstalado, hubiese optado por Just, ya que es el menos pesado.  