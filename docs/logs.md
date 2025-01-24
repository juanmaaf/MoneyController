# Elección de herramienta para registro de actividad (LOGS)

Para poder añadir a los programas implementados el servicio esencial de registro de actividad, el primer paso es elegir una herramienta que se encargue de este servicio. Para la búsqueda de herramientas, he buscado en foros de Reddit como [Registro de Python: ¿hay una mejor opción?](https://www.reddit.com/r/Python/comments/uk5c49/python_logging_is_there_a_best_choice/?rdt=37687) o [¿Hay alguna buena biblioteca de registro JSON para Python?](https://www.reddit.com/r/learnpython/comments/701nif/are_there_any_good_json_logging_libraries_for/). A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto. 

## Criterios de selección

1. Se considerará que la herramienta esté bien mantenida y actualizada. Podremos verificar este criterio de forma objetiva basándonos en la página [GitHub](https://github.com/) de cada herramienta. Esto permite evitar aumentar la deuda técnica del proyecto.    
2. Intentar reducir las dependencias. Se considerará que la herramienta añada la menor cantidad posible de dependencias al proyecto.  

## Comparación de herramientas

1. **Logging estándar de Python**:  
    [Documentación Python](https://docs.python.org/3/library/logging.html)  
    Es parte de la biblioteca de Python, por lo que está mantenida y actualizada en cada versión de Python. No añade dependencias al proyecto, ya que está incluida en la biblioteca de Python.

2. **Loguru**:  
    [Loguru](https://github.com/Delgan/loguru)  
    Es una herramienta activa con actualizaciones frecuentes, como podemos ver en su repositorio de GitHub. Su última versión se publicó hace un mes. Podemos ver las dependencias que requiere en [Pyproject.toml](https://github.com/Delgan/loguru/blob/master/pyproject.toml). Requiere instalarse como paquete. En el apartado `dependecies` podemos ver que hay 3 dependencias. 2 son para SO Windows (`colorama` y `win32-setctime`), y la otra para versiones de Python inferiores a la 3.7 (`aiocontextvars`). Ninguna de estas dependencias se aplica a nuestro proyecto. En el bloque `build-system` podemos ver que requiere la dependencia de construcción `flit_core`.     

3. **Structlog**:  
    [Structlog](https://github.com/hynek/structlog/)  
    Es una herramienta activa con actualizaciones frecuentes, como podemos ver en su repositorio de GitHub. Su última versión se publicó hace una semana. Podemos ver las dependencias que requiere en [Pyproject.toml](https://github.com/hynek/structlog/blob/main/pyproject.toml). Requiere instalarse como paquete. En el apartado `dependecies` podemos ver que hay 1 depencencia para versiones de Python inferiores a la 3.11 (`typing-extensions`). Esta dependencia no se aplica a nuestro proyecto. En el bloque `build-system` podemos ver que requiere las dependencias de cosntrucción: `hatchling`, `hatch-vcs` y `hatch-fancy-pypi-readme`.  

4. **Logbook**:  
    [Logbook](https://github.com/getlogbook/logbook)  
    Es una herramienta que nació para ser una alternativa moderna. Como podemos ver en su repositorio de GitHub, su última versión se publicó hace un mes. No obstante el nivel de actividad ha disminuido. En 2023 se lanzaron 3 versiones, y en 2024 una en diciembre, por lo que la frecuencia de actualización ha disminuido considerablemente. Podemos ver las dependencias que requiere en [Pyproject.toml](https://github.com/getlogbook/logbook/blob/develop/pyproject.toml). Requiere instalarse como paquete. En el bloque `build-system` podemos ver que requiere las dependencias de construcción: `setuptools` y `Cython`.  

5. **Python-JSON-Logger**:  
    [Python-JSON-Logger](https://github.com/nhairs/python-json-logger)  
    Es una herramienta activa con actualizaciones frecuentes, como podemos ver en su repositorio de GitHub. Su última versión se publicó hace un mes. Podemos ver las dependencias que requiere en [Pyproject.toml](https://github.com/nhairs/python-json-logger/blob/main/pyproject.toml). Requiere instalarse como paquete. En el apartado `dependecies` podemos ver que hay 1 depencencia para versiones de Python inferiores a la 3.10 (`typing-extensions`). Esta dependencia no se aplica a nuestro proyecto. En el bloque `build-system` podemos ver que requiere la dependencia de construcción: `setuptools`.  

## Conclusión

Tras evaluar las diferentes herramientas de registro de actividad en función de los criterios de mantenimiento y actualización y reducción de dependencias, la elección más adecuada para este proyecto es **Loguru**.

Aunque Loguru introduce una dependencia en su bloque `build-system`, además de la instalación del paquete, su ventaja principal radica en ser una herramienta moderna y activa y altamente flexible. Esto la convierte en una opción ideal para proyectos como el que se desarrolla en este repositorio.

El nivel de actividad y las actualizaciones regulares de Loguru demuestran que el proyecto está bien mantenido, lo que asegura la longevidad de la herramienta en el tiempo. Por lo tanto, **Loguru** se ajusta mejor a las necesidades del proyecto, proporcionando una solución robusta y fácil de usar para gestionar los logs de manera eficiente.