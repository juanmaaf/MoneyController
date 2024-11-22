# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Automatización de tareas personalizada**: Debe permitir la definición y automatización de tareas específicas, como pruebas y verificación de estilo de código, además de gestionar dependencias entre tareas, sin estar restringida a ámbitos específicos.   
- **Baja complejidad**: La herramienta debe ser simple y no debe añadir complejidad al desarrollo del proyecto. 
- **Actualizaciones recientes**: Se priorizan herramientas activamente mantenidas para asegurar compatibilidad futura y resolver posibles problemas técnicos.   

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares: Invoke, Make y Fabric. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke)  
   - **Automatización**: Permite la automatización de tareas personalizadas de manera flexible usando Python. Ideal para tareas como pruebas, verificación de estilo, y más.  
   - **Complejidad**: Aunque es poderoso, requiere cierta configuración inicial y programación en Python, lo que puede ser excesivo para tareas básicas. 
   - **Actualizaciones**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Automatización**: Muy flexible y potente, ideal para proyectos con tareas complejas y dependencias. Utiliza una sintaxis simple y clara para definir las reglas de ejecución.  
   - **Complejidad**: Configuración simple en un único archivo `Makefile`. No requiere programación adicional.  
   - **Actualizaciones**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas.    

3. **Fabric**: 
   [Fabric](https://github.com/fabric/fabric)   
   - **Automatización**: Ideal para ejecutar tareas de automatización remota, como despliegues y administración de servidores. Permite definir tareas en Python.  
   - **Complejidad**: Está más orientado a tareas de administración remota, lo que lo hace innecesariamente complejo para tareas locales simples.  
   - **Actualizaciones**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en proyectos simples, debido a su simplicidad, capacidad de automatización de tareas locales y mínima configuración. Invoke, aunque más potente, requiere configuración en Python, lo que lo hace innecesario para tareas simples. Fabric, orientado a la automatización remota, resulta excesivo para este tipo de proyectos.    