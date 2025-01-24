# Elección de herramienta para registro de actividad (LOGS)

Para poder añadir a los programas implementados el servicio esencial de registro de actividad, el primer paso es elegir una herramienta que se encargue de este servicio. Para la búsqueda de herramientas, he buscado en foros de Reddit como [Registro de Python: ¿hay una mejor opción?](https://www.reddit.com/r/Python/comments/uk5c49/python_logging_is_there_a_best_choice/?rdt=37687) o [¿Hay alguna buena biblioteca de registro JSON para Python?](https://www.reddit.com/r/learnpython/comments/701nif/are_there_any_good_json_logging_libraries_for/). A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto. 

## Criterios de selección

1. Se considerará que la herramienta esté bien mantenida y actualizada. Podremos verificar este criterio de forma objetiva basándonos en la página [GitHub](https://github.com/) de cada herramienta. Esto permite evitar aumentar la deuda técnica del proyecto.    
2. Intentar reducir las dependencias. Se considerará que la herramienta añada la menor cantidad posible de dependencias al proyecto.  

## Comparación de herramientas

1. **Logging estándar de Python**:  
    [Documentación Python](https://docs.python.org/3/library/logging.html)  

2. **Loguru**:  
    [Loguru](https://github.com/Delgan/loguru)  

3. **Structlog**:  
    [Structlog](https://github.com/hynek/structlog/)  

4. **Logbook**:  
    [Logbook](https://github.com/getlogbook/logbook)

5. **Python-JSON-Logger**:  
    [Python-JSON-Logger](https://github.com/nhairs/python-json-logger)  

## Conclusión