# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

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
   `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas, con una comunidad muy amplia.  

3. **Task**: 
   [Task](https://github.com/go-task/task)    
   Es un proyecto activo, con soporte continuo y buen mantenimiento. Tiene una comunidad en continuo crecimiento. Tiene una gran valoración su repositorio de GitHub. 

4. **Just**: 
   [Just](https://github.com/casey/just)   
   Es un proyecto activo y bien mantenido, con actualizaciones regulares. Tiene una gran valoración su repositorio de GitHub. 
   
## Conclusión

De todas las herramientas comparadas, descarto inicialmente Invoke, ya que es la que tiene un mantenimiento inactivo como bien podemos ven en su página de Snyk Advisor. 

Finalmente, entre Make, Task y Just, podría elegir cualquiera de las herramientas, dado que cumplen los requisitos. Son herramientas estables y bien mantenidsa. Por experiencia y conocimiento de la herramienta, elijo **Make** como gestor de tareas del proyecto que se desarrolla en este repositorio. 