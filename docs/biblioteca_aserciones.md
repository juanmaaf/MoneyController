# Biblioteca de Aserciones

Para la elección de la biblioteca de aserciones, he buscado y evaluado las distintas alternativas posibles. He buscado herramientas en [Snyk Advisor](https://snyk.io/advisor/) y en foros de Reddit como [Is there life beyond PyUnit/PyTest?](https://www.reddit.com/r/Python/comments/1h0yg58/is_there_life_beyond_pyunitpytest/) y [Anyone working on or with a great but little-known test framework? ](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/). A continuación detallo los criterios específicos que he tenido en cuenta para la elección de la herramienta. 

- Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva. 
- Se considerarán las herramientas que tengan actualizaciones recientes y estables. Para poder valorar este criterio con objetividad, se tendrá en cuenta el número de versiones de Python 3.x.0 (actualización mayor que hace Python cada año), siendo la actual la 3.13.0, que se han realizado hasta que la herramienta se haya actualizado. Podemos verificarlo viendo en las páginas de [Snyk Advisor](https://snyk.io/advisor/) y [PyPi](https://pypi.org/) si las últimas versiones disponibles de cada herramienta son recientes. Podemos ver las actualizaciones de Python en su documentación oficial [Actualizaciones Python](https://www.python.org/doc/versions/).
- Intentar reducir las dependencias. Se considerará no añadir dependencias al proyecto si la propia biblioteca de Python ofrece aserciones que cumplen con todos los requisitos establecidos. 

# Comparación de Herramientas

1. **Unittest (PyUnit)**:
    [Página oficial Python](https://github.com/python/cpython/tree/main/Lib/unittest)  
    [Documentación oficial Python](https://docs.python.org/es/3/library/unittest.html)   
    Como parte de la biblioteca estándar de Python, es una herramienta ampliamente utilizada y considerada un estándar del lenguaje. No aparece en Snyk Advisor ni es evaluado en foros ya que es una biblioteca que Python incluye. Su soporte activo está garantizado por el equipo de Python.  

2. **Grappa**:
    [Snyk Advisor](https://snyk.io/advisor/python/grappa)  
    [PyPi](https://pypi.org/project/grappa/)  
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación (51/100) y además su última versión se publicó hace 4 años, 4 versiones de Pyhton atrás, versión 3.9.0. 

3. **PyHamCrest**:
    [Snyk Advisor](https://snyk.io/advisor/python/pyhamcrest)  
    [PyPi](https://pypi.org/project/PyHamcrest/)  
    Como podemos ver en su página de Snyk Advisor, a pesar de tener una puntuación media alta (72/100) y que su última versión se publicase hace un año, una versión de Python atrás, versión 3.12.0, el proyecto ya se cataloga como inactivo, lo que nos lleva a la conclusión de no tenerla en cuenta.  

4. **Expects**:
    [Snyk Advisor](https://snyk.io/advisor/python/expects)  
    [PyPi](https://pypi.org/project/expects/)    
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación (52/100) y además su última versión se publicó hace 2 años, 2 versiones de Python atrás, versión 3.11.0.  

5. **Ensure**:
    [Snyk Advisor](https://snyk.io/advisor/python/ensure)  
    [PyPi](https://pypi.org/project/ensure/)  
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación (53/100), lo que nos lleva a la conclusión de no tenerla en cuenta. Sí es cierto que su última versión se publicó hace un año, 1 versión de Python atrás, versión 3.12.0, pero el proyecto ya se cataloga como inactivo.    

6. **Behave**:
    [Snyk Advisor](https://snyk.io/advisor/python/behave)  
    [PyPi](https://pypi.org/project/behave/)  
    Como podemos ver en su página de Snyk Advisor, tiene una puntuación media-alta (83/100). Además, su última versión se publicó hace 7 años, 7 versiones de Python atrás, versión 3.6.0. No obstante, no se cataloga el proyecto como inactivo y tiene commits recientes, lo que nos hace tener en cuenta esta herramienta. Tiene un enfoque BDD. 

# Conclusión

Teniendo en cuenta los criterios formulados y las herramientas comparadas, las mejores opciones son Unittest y Behave. La primera está incluida en la biblioteca de Python, ofrece soporte activo y cumple con los requisitos básicos de aserciones. Behave es una herramienta que define pruebas con un enfoque BDD. Aunque su última versión se publicase hace 7 años, tiene commits recientes y no se cataloga como inactivo en Snyk. Herramientas como Grappa, PyHamCrest, Expects y Ensure presentan desventajas significativas, como falta de actualizaciones recientes o baja puntuación en [Snyk Advisor](https://snyk.io/advisor/), lo que hace que las descarte. Finalmente, entre Unittest y Behave, elijo **Unittest** ya que además de cumplir con el resto de requisitos, forma parte de la librería de Python, lo que implica que no añada dependencias al proyecto.  
