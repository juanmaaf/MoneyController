# Test Runner

Para la elección del test runner, he buscado y evaluado las distintas alternativas posibles. 
He buscado herramientas en [Snyk Advisor](https://snyk.io/advisor/) y en foros de Reddit como [Is there life beyond PyUnit/PyTest?](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/) y [Anyone working on or with a great but little-known test framework? ](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/). 
A continuación detallo los criterios específicos que he tenido en cuenta para la elección de la herramienta, similares a los establecidos para la elección de la biblioteca de aserciones. 

- Se considerarán las herramientas que tengan una buena puntuación en [Snyk Advisor](https://snyk.io/advisor/).
- Se considerarán las herramientas que tengan actualizaciones recientes valorando este criterio en función del número de actualizaciones de Python que han pasado hasta que la herramienta se haya actualizado. Podemos verificarlo viendo en las páginas de [Snyk Advisor](https://snyk.io/advisor/) y [PyPi](https://pypi.org/) si las últimas versiones disponibles de cada herramienta son recientes. Podemos ver las actualizaciones de Python en su documentación oficial [Actualizaciones Python](https://www.python.org/doc/versions/).
- Se considerará si existe un estándar en el lenguaje de programación.   
- Se considerará que la herramienta tenga un sistema de fixtures y proporcione salidas detalladas. 

# Comparación de Herramientas

1. **Pytest**:
    [Snyk Advisor](https://snyk.io/advisor/python/pytest)    
    [PyPi](https://pypi.org/project/pytest/)   
    Pytest es uno de los test runners más populares y usados en proyectos desarrollados en Python. Ofrece soporte para fixtures y proporciona salidas detalladas. En su página de Snyk Advisor podemos ver que tiene una alta puntuación, el proyecto tiene soporte activo y presenta actualizaciones recientes, coincidiendo con la última actualización de Python.  

2. **Unittest (PyUnit)**:
    [Página oficial Python](https://github.com/python/cpython/tree/main/Lib/unittest)  
    [Documentación oficial Python](https://docs.python.org/es/3/library/unittest.html)   
    Unittest es una biblioteca que forma parte de Pyhton y es el framework de pruebas estándar de Python. Incluye un test runner básico orientado a la ejecución de pruebas unitarias. Tiene un soporte activo pero es más limitado que Pytest en cuanto a fixtures y salidas detalladas.  

3. **Nose2**:
    [Snyk Advisor](https://snyk.io/advisor/python/nose2)    
    [PyPi](https://pypi.org/project/nose2/)    
    Nose2 es una extensión de Unittest e incluye características que lo hacen más flexible y avanzado. No obstante, si vemos su página de Snyk Advisor, a pesar de tener una puntuación media-alta y de tener una última versión publicada hace 6 meses, coincidiendo con la última actualización de Python, el proyecto está catalogado como inactivo.  

4. **Hammett**:
    [Snyk Advisor](https://snyk.io/advisor/python/hammett)  
    [PyPi](https://pypi.org/project/hammett/)        
    Hammet es un test runner que, como podemos ver en su página de Snyk Advisor, indica que es mucho más rápido que Pytest, justificando la afirmación con comparacions detalladas. Sin embargo, aunque el proyecto no está catalogado como inactivo, tiene una baja puntuación y una comunidad limitada. 

# Conclusión

Finalmente, entre todas las opciones elegiré **Pytest**. Descarto Unittest ya que a pesar de ser el framework estándar de pruebas no es un test runner. El test runner que incluye la herramienta es bastante básico, orientado a pruebas unitarias. Descarto Nose2 porque, aunque es más avanzado e incluye funcionalidades que no tiene Unittest, podemos ver en su página de Snyk Advisor que su proyecto está inactivo, por lo que no tiene soporte. Finalmente, Hammett es un test runner moderno y poco conocido que es más rápido que Pytest. Sin embargo, tiene una baja puntuación en Snyk Advisor y una comunidad muy limitada.  

# Comando para ejecutar los Test

Finalmente, elegidos biblioteca de aserciones y test runner necesitamos la elección final del comando que ejecutará estos test. Tenemos que evaluar las distintas Herramientas CLI disponibles para ejecutar los test. De las herramientas que hemos evaluado como test runner, solo Pytest y Nose2 son herramientas CLI, ya que analizan la salida TAP y producen un informe detallado con los resultados del test. Hammet es una herramienta CLI pero se fundamenta en la velocidad en lugar de en documentar los resultados, como podemos ver e su página de Snyk [Hammet Snyk](https://snyk.io/advisor/python/hammett). Por tanto, entre Pytest y Nose2, elegiré **Pytest** ya que el proyecto Nose2 está catalogado comi inactivo en su página de Snyk Advisor [Nose2 Snyk](https://snyk.io/advisor/python/nose2).


