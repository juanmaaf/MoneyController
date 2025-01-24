# Elección de herramienta para configuración

Para poder añadir a los programas implementados el servicio esencial de uso de configuración, el primer paso es elegir una herramienta que se encargue de este servicio. Para la búsqueda de herramientas, he buscado en foros de Reddit como [¿Cuál es la mejor práctica para inyectar configuración en una aplicación de Python?](https://www.reddit.com/r/Python/comments/u0j5rn/what_is_the_best_practice_for_injecting/) o [Deja de codificar en duro y empieza a usar archivos de configuración en su lugar, requiere muy poco esfuerzo con configparser](https://www.reddit.com/r/Python/comments/my1m66/stop_hardcoding_and_start_using_config_files/). A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto. 

## Criterios de selección

1. Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva.  
2. Se considerará que la herramienta esté bien mantenida y actualizada, permitiendo evitar aumentar la deuda técnica del proyecto.    

## Comparación de herramientas

1. **Dynaconf**:  
    [Snyk Advisor](https://snyk.io/advisor/python/dynaconf)  
    [GitHub](https://github.com/dynaconf/dynaconf)  

2. **Pydantic**:  
    [Snyk Advisor](https://snyk.io/advisor/python/pydantic)  
    [GitHub](https://github.com/pydantic/pydantic)  

3. **Configparser**:  
    [Snyk Advisor](https://snyk.io/advisor/python/configparser)  
    [GitHub](https://github.com/jaraco/configparser)  

4. **Python-dotenv**:  
    [Snyk Advisor](https://snyk.io/advisor/python/python-dotenv)  
    [GitHub](https://github.com/theskumar/python-dotenv)  

5. **Dependecy-injector**:  
    [Snyk Advisor](https://snyk.io/advisor/python/dependency-injector)  
    [GitHub](https://github.com/ets-labs/python-dependency-injector)    

## Conclusión