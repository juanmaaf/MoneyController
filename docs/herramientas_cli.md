# Herramientas CLI para ejecutar los test

Para la elección del comando para ejecutar los test he buscado y evaluado las distintas alternativas posibles. Para ello, me he basado en los criterios específicos que detallo a continuación. 

- Se considerarán las herramientas que tengan una alta puntuación en [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación est
a basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Se considerará esta puntuación como el nivel de salud de la herramienta. 
- Se considerarán las herramientas que tengan actualizaciones recientes y estables. Para poder valorar este criterio con objetividad, tendrá en cuenta el número de versiones de Python 3.x.0 (actualización mayor que hace Python cada año), siendo la actual la 3.13.0, que se han realizado hasta que la herramienta se haya actualizado. Podemos verificarlo viendo en las páginas de [Snyk Advisor](https://snyk.io/advisor/) y [PyPi](https://pypi.org/) si las últimas versiones disponibles de cada herramienta son recientes. Podemos ver las actualizaciones de Python en su documentación oficial [Actualizaciones Python](https://www.python.org/doc/versions/).  
- Se considerarán los test runners evaluados en [Test Runners](/docs/test_runner.md).  

# Comparación de herramientas

1. **Pytest**:
    [Snyk Advisor](https://snyk.io/advisor/python/pytest)     
    [PyPi](https://pypi.org/project/pytest/)    
    Pytest es uno de los test runners más populares y usados en proyectos desarrollados en Python. Ofrece soporte para fixtures y proporciona salidas detalladas. En su página de Snyk Advisor podemos ver que tiene una alta puntuación, el proyecto tiene soporte activo y presenta actualizaciones recientes, coincidiendo con la última actualización de Python.   

2. **Nose2**:
    [Snyk Advisor](https://snyk.io/advisor/python/nose2)    
    [PyPi](https://pypi.org/project/nose2/)    
    Nose2 es un framework de pruebas compatible con Unittest e incluye características que lo hacen más flexible y avanzado. No obstante, si vemos su página de Snyk Advisor, a pesar de tener una puntuación media-alta y de tener una última versión publicada hace 6 meses, coincidiendo con la última versión de Python, versión 3.13.0, el proyecto está catalogado como inactivo.  

# Conclusión

Finalmente, elegidos biblioteca de aserciones y test runner necesitamos la elección final del comando que ejecutará estos test. De las herramientas que hemos evaluado como test runner, solo Pytest y Nose2 son herramientas CLI, ya que analizan la salida TAP y producen un informe detallado con los resultados del test. Hammet es una herramienta CLI pero se fundamenta en la velocidad en lugar de en documentar los resultados, como podemos ver e su página de Snyk [Hammet Snyk](https://snyk.io/advisor/python/hammett). Por tanto, entre Pytest y Nose2, elegiré **Pytest** ya que el proyecto Nose2 está catalogado comi inactivo en su página de Snyk Advisor [Nose2 Snyk](https://snyk.io/advisor/python/nose2).  