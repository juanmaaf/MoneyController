# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- La herramienta debe un peso en espacio de almacenamieto bajo para no aumentar el espacio necesario en la máquina para el desarrollo del proyecto. Podemos comprobar este criterio en la página de GitHub de cada herramienta comprobando el peso de la versión más reciente. Se considerará que la herramienta esté instalada en el Sistema Operativo que desarrolla el proyecto.   
- Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva. 
- Si no tiene página de [Snyk Advisor](https://snyk.io/advisor/), se considerará que la herramienta sea actualizada regularmente y mantenida. Podremos verificar este criterio de forma objetiva basándonos en las páginas de [GitHub](https://github.com/) de cada herramienta.  

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas populares: Invoke, Make, Task y Just. La comparación se basa en los criterios específicos establecidos.  

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke) 
   [Invoke Snyk](https://snyk.io/advisor/python/invoke) 
   Como podemos ver en su página de Snyk Advisor, a pesar de tener una puntuación media-alta (76/100) el proyecto Invoke está catalogado como Inactivo. Además, su última versión se publicó hace 2 años. 

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia. El tamaño de su última versión (4.4.1), publicada en Febrero de 2023, en formato tar.gz, es 950 KB. 

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   Es un proyecto activo, con soporte continuo y buen mantenimiento. Tiene una comunidad en continuo crecimiento. El tamaño de su última versión (3.40.1), publicada en Diciembre de 2024, en formato tar.gz, es 486 KB. 

4. **Just**: 
   [Just](https://github.com/casey/just)   
   Es un proyecto activo y bien mantenido, con actualizaciones regulares. El tamaño de su última versión (1.38.0), publicada en Diciembre de 2024, en formato tar.gz, es 689 KB. 
   
## Conclusión

De todas las herramientas comparadas, descarto inicialmente Invoke, ya que es la que tiene un mantenimiento inactivo como bien podemos ven en su página de Snyk Advisor. 

Finalmente, entre Make, Task y Just, dado que desarrollo el proyecto en una máquina Ubuntu donde Make viene preinstalado y no ocasiona espacio adicional, elijo **Make** como gestor de tareas del proyecto que se desarrolla en este repositorio. Además, cumple con los criterios establecidos, ya que es una herramienta muy conocida mantenida durante décadas. Garantiza fiabilidad. En caso de desarrollar este proyecto en una máquina con otro sistema operativo, donde Make no estuviese preinstalado, hubiese optado por Task, ya que es el menos pesado, y también cumple con los criterios establecidos.  