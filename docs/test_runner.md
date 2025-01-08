# Test Runner

Para la elección del test runner, he buscado y evaluado las distintas alternativas posibles. 
He buscado herramientas en [Snyk Advisor](https://snyk.io/advisor/) y en foros de Reddit como [Is there life beyond PyUnit/PyTest?](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/) y [Anyone working on or with a great but little-known test framework? ](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/). 
A continuación detallo los criterios específicos que he tenido en cuenta para la elección de la herramienta, similares a los establecidos para la elección de la biblioteca de aserciones. 

- Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva.  
- Se considerarán las herramientas que tengan actualizaciones recientes y estables. Para poder valorar este criterio con objetividad, se tendrá en cuenta el número de versiones de Python 3.x.0 (actualización mayor que hace Python cada año), siendo la actual la 3.13.0, que se han realizado hasta que la herramienta se haya actualizado. Podemos verificarlo viendo en las páginas de [Snyk Advisor](https://snyk.io/advisor/) y [PyPi](https://pypi.org/) si las últimas versiones disponibles de cada herramienta son recientes. Podemos ver las actualizaciones de Python en su documentación oficial [Actualizaciones Python](https://www.python.org/doc/versions/).  
- Se considerará si existe un estándar en Python.  

# Comparación de Herramientas

1. **Pytest**:
    [Snyk Advisor](https://snyk.io/advisor/python/pytest)    
    [PyPi](https://pypi.org/project/pytest/)   
    Pytest es uno de los test runners más populares y usados en proyectos desarrollados en Python. Ofrece soporte para fixtures y proporciona salidas detalladas. En su página de Snyk Advisor podemos ver que tiene una alta puntuación, el proyecto tiene soporte activo y presenta actualizaciones recientes, coincidiendo con la última versión de Python, versión 3.13.0.  

2. **Unittest (PyUnit)**:
    [Página oficial Python](https://github.com/python/cpython/tree/main/Lib/unittest)  
    [Documentación oficial Python](https://docs.python.org/es/3/library/unittest.html)   
    Unittest es una biblioteca que forma parte de Pyhton y es el framework de pruebas estándar de Python. Incluye un test runner básico orientado a la ejecución de pruebas unitarias. Tiene un soporte activo pero es más limitado que Pytest en cuanto a fixtures y salidas detalladas.  

3. **Nose2**:
    [Snyk Advisor](https://snyk.io/advisor/python/nose2)    
    [PyPi](https://pypi.org/project/nose2/)    
    Nose2 es un framework de pruebas compatible con Unittest e incluye características que lo hacen más flexible y avanzado. No obstante, si vemos su página de Snyk Advisor, a pesar de tener una puntuación media-alta y de tener una última versión publicada hace 6 meses, coincidiendo con la última versión de Python, versión 3.13.0, el proyecto está catalogado como inactivo.  

4. **Hammett**:
    [Snyk Advisor](https://snyk.io/advisor/python/hammett)  
    [PyPi](https://pypi.org/project/hammett/)        
    Hammet es un test runner que, como podemos ver en su página de Snyk Advisor, indica que es mucho más rápido que Pytest, justificando la afirmación con comparacions detalladas. Sin embargo, aunque el proyecto no está catalogado como inactivo, tiene una baja puntuación y una comunidad limitada. 

# Conclusión

Finalmente, entre todas las opciones elegiré **Pytest**. Descarto Unittest ya que a pesar de ser el framework estándar de pruebas no es un test runner. El test runner que incluye la herramienta es bastante básico, orientado a pruebas unitarias. Descarto Nose2 porque, aunque es más avanzado e incluye funcionalidades que no tiene Unittest, podemos ver en su página de Snyk Advisor que su proyecto está inactivo, por lo que no tiene soporte. Finalmente, Hammett es un test runner moderno y poco conocido que es más rápido que Pytest. Sin embargo, tiene una baja puntuación en Snyk Advisor y una comunidad muy limitada.  


