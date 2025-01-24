# Elección de herramienta para configuración

Para poder añadir a los programas implementados el servicio esencial de uso de configuración, el primer paso es elegir una herramienta que se encargue de este servicio. Para la búsqueda de herramientas, he buscado en foros de Reddit como [¿Cuál es la mejor práctica para inyectar configuración en una aplicación de Python?](https://www.reddit.com/r/Python/comments/u0j5rn/what_is_the_best_practice_for_injecting/) o [Deja de codificar en duro y empieza a usar archivos de configuración en su lugar, requiere muy poco esfuerzo con configparser](https://www.reddit.com/r/Python/comments/my1m66/stop_hardcoding_and_start_using_config_files/). A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto. 

## Criterios de selección

1. Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva.  
2. Se considerará que la herramienta esté bien mantenida y actualizada, permitiendo evitar aumentar la deuda técnica del proyecto.    

## Comparación de herramientas

1. **Dynaconf**:  
    [Snyk Advisor](https://snyk.io/advisor/python/dynaconf)  
    [GitHub](https://github.com/dynaconf/dynaconf)  
    Como podemos ver en su página de Snyk Advisor, tiene una alta puntuación (97/100), destacando en los 4 criterios. Como podemos ver en su repositorio de GitHub, es una herramienta activa y mantenida, con una última versión publicada hace 3 días.  

2. **Pydantic**:  
    [Snyk Advisor](https://snyk.io/advisor/python/pydantic)  
    [GitHub](https://github.com/pydantic/pydantic)  
    Como podemos ver en su página de Snyk Advisor, tiene una alta puntuación (94/100), destacando en los 4 criterios. Como podemos ver en su repositorio de GitHub, es una herramienta activa y mantenida, con una última versión publicada hace menos de 1 día.  

3. **Configparser**:  
    [Snyk Advisor](https://snyk.io/advisor/python/configparser)  
    [GitHub](https://github.com/jaraco/configparser)  
    Como podemos ver en su página de Snyk Advisor, tiene una media-alta puntuación (82/100), teniendo una peor puntuación en el criterio correspondiente a la comunidad. Como podemos ver en su repositorio de GitHub, es una herramienta activa y mantenida, con una última versión publicada en agosto de 2024.  

4. **Python-dotenv**:  
    [Snyk Advisor](https://snyk.io/advisor/python/python-dotenv)  
    [GitHub](https://github.com/theskumar/python-dotenv)  
    Como podemos ver en su página de Snyk Advisor, tiene una media-alta puntuación (84/100), teniendo una peor puntuación en el criterio correspondiente al mantenimiento, catalogado como `Sustainable`. Como podemos ver en su repositorio de GitHub, su última versión fue publicada en enero de 2024, bajando el nivel de actividad respecto a años anteriores donde se publicaban 2 versiones por año.   

5. **Dependecy-injector**:  
    [Snyk Advisor](https://snyk.io/advisor/python/dependency-injector)  
    [GitHub](https://github.com/ets-labs/python-dependency-injector)    
    Como podemos ver en su página de Snyk Advisor, tiene una media-alta puntuación (85/100), teniendo una peor puntuación en el criterio correspondiente a la comunidad. Como podemos ver en su repositorio de GitHub, es una herramienta activa y mantenida, con una última versión publicada hace 3 semanas.  

## Conclusión

Basándonos en los criterios establecidos, **Dynaconf** es la herramienta más adecuada. Tiene la puntuación más alta en Snyk Advisor (97/100), destacando en todos los aspectos evaluados, y su mantenimiento es sobresaliente, con una versión publicada hace solo 3 días.  

Otras opciones como Pydantic y Dependency-injector también cumplen los criterios establecidos, tienen una alta puntuación y son herramientas activas y mantenidas. Podrían ser elegidas. 

Por tanto, dado que es la herramienta con mayor puntuación en Snyk Advisor, **Dynaconf** es la herramienta que mejor se ajusta a los objetivos del proyecto que se desarrolla en este repositorio y es la herramienta de configuración que elijo.