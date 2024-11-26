# Gestor de Tareas

Para la automatización de tareas en este proyecto de Python, he evaluado distintas opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- **Soporte para todo tipo de tareas**: La herramienta no debe estar restringida a tareas de un tipo específico, sino que debe ofrecer flexibilidad para gestionar cualquier tipo de tarea necesaria en el proyecto.    
- **Baja complejidad**: La herramienta debe ser adecuada para el alcance del proyecto y no debe añadir complejidad innecesaria al desarrollo. 
- **Actualizaciones recientes**: Se priorizan herramientas activamente mantenidas para asegurar compatibilidad futura y resolver posibles problemas técnicos.   

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron tres herramientas populares: Invoke, Make y Task. Además, se considerará la opción de gestionar las tareas mediante scripts de Python. La comparación se basa en los criterios específicos establecidos.

1. **Invoke**: 
   [Invoke](https://github.com/pyinvoke/invoke)  
   - **Soporte**: Es flexible y permite definir prácticamente cualquier tipo de tarea, sin estar limitada a un ámbito específico.    
   - **Complejidad**: Requiere programación en Python, lo que puede ser una ventaja al tratarse de un proyecto en Python, y cierta configuración inicial, lo que puede ser excesivo para tareas básicas. 
   - **Actualizaciones**: El proyecto de `Invoke` ha tenido una disminución en su actividad, con la última actualización significativa en 2023.  

2. **Make**: 
   [Make](https://github.com/mirror/make)  
   - **Soporte**: Es flexible y permite ejecutar comandos para cualquier tipo de tarea.  
   - **Complejidad**: Configuración en un único archivo `Makefile`. No requiere programación adicional.  
   - **Actualizaciones**: `Make` es una herramienta establecida que ha sido activamente mantenida durante décadas, asegurando una alta fiabilidad y compatibilidad futura sin problemas.    

3. **Task**: 
   [Task](https://github.com/go-task/task)   
   - **Soporte**: Requiere adaptaciones adicionales para ciertos tipos de tareas específicas de Python.  
   - **Complejidad**: Es fácil de usar y configurar. Requiere la instalación de herramientas adicionales.  
   - **Actualizaciones**: Es un proyecto activo, con soporte continuo y compatible con múltiples plataformas, lo que asegura un buen mantenimiento futuro. 

4. **Gestión de tareas con scripts de Python**:  
   - **Soporte**: Flexibilidad total en proyectos de alcance similar al que se desarrolla en este repositorio. Se reduce el orden y la escalabilidad en proyectos más grandes.  
   - **Complejidad**: Requieren aprender y trabajar directamente con la interfaz de Python, lo que introduce un nivel innecesario de complejidad.    
   - **Actualizaciones**: Dependen de la versión de Python instalada en el entorno.     
   
## Conclusión

**Make** es la opción más adecuada para gestionar tareas en este proyecto, debido a su flexibilidad y mínima configuración. Otras opciones, como Invoke, Fabric, Task, o el uso de scripts en Python, son más complejas o requieren configuraciones adicionales innecesarias para este caso. Make ofrece la solución más práctica y directa para las necesidades del proyecto.  