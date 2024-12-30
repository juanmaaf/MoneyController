# Biblioteca de Aserciones

Para la elección de la biblioteca de aserciones, he buscado y evaluado las distintas alternativas posibles. He buscado herramientas en [Snyk Advisor](https://snyk.io/advisor/) y en foros de Reddit como [Is there life beyond PyUnit/PyTest?](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/) y [Anyone working on or with a great but little-known test framework? ](https://www.reddit.com/r/Python/comments/1gbxrho/anyone_working_on_or_with_a_great_but_littleknown/). A continuación detallo los criterios específicos que he tenido en cuenta para la elección de la herramienta. 

- Se considerarán las herramientas que tengan una alta puntuación en [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación est
a basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Se considerará esta puntuación como el nivel de salud de la herramienta. 
- Se considerarán las herramientas que tengan actualizaciones recientes y estables. Para poder valorar este criterio con objetividad, tendrá en cuenta el número de versiones de Python 3.x.0 (actualización mayor que hace Python cada año), siendo la actual la 3.13.0, que se han realizado hasta que la herramienta se haya actualizado. Podemos verificarlo viendo en las páginas de [Snyk Advisor](https://snyk.io/advisor/) y [PyPi](https://pypi.org/) si las últimas versiones disponibles de cada herramienta son recientes. Podemos ver las actualizaciones de Python en su documentación oficial [Actualizaciones Python](https://www.python.org/doc/versions/).  
- Se considerará que la herramienta ofrezca diferentes tipos de aserciones, como los tipos (igualdad, veracidad, mayor/menor, etc.), aserciones específicas de excepciones, o enfoques BDD (como should o expect). Esto evitará deuda técnica innecesaria en el futuro, permitiendo escribir pruebas específicas sin tener que implemenar la lógica de la aserción.  
- Se considerará si existe una biblioteca de aserciones en la biblioteca de Python.   

# Comparación de Herramientas

1. **Assert nativo de Python**:
    [Documentación oficial Python](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)  
    Ofrece una funcionalidad básica y directa para realizar aserciones en Python sin dependencias externas, ya que forma parte de la biblioteca estándar de Python. No ofrece tipos de aserciones ya que se limita a la línea de código iniciada por `assert`. No aparece en Snyk Advisor ni es evaluado en foros ya que forma parte de Python. 

2. **Unittest (PyUnit)**:
    [Página oficial Python](https://github.com/python/cpython/tree/main/Lib/unittest)  
    [Documentación oficial Python](https://docs.python.org/es/3/library/unittest.html)   
    Como parte de la biblioteca estándar de Python, es una herramienta ampliamente utilizada y considerada un estándar del lenguaje. Como podemos ver en los distintos métodos assert que ofrece [TestCase](https://docs.python.org/es/3/library/unittest.html#unittest.TestCase), ofrece distintos tipos de aserciones. No aparece en Snyk Advisor ni es evaluado en foros ya que es una biblioteca que Python incluye. Su soporte activo está garantizado por el equipo de Python.  

3. **Grappa**:
    [Snyk Advisor](https://snyk.io/advisor/python/grappa)  
    [PyPi](https://pypi.org/project/grappa/)  
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación y además su última versión se publicó hace 4 años, 4 versiones de Pyhton atrás, versión 3.9.0. 

4. **PyHamCrest**:
    [Snyk Advisor](https://snyk.io/advisor/python/pyhamcrest)  
    [PyPi](https://pypi.org/project/PyHamcrest/)  
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación, lo que nos lleva a la conclusión de no tenerla en cuenta. Sí es cierto que su última versión se publicó hace un año, 1 versión de Python atrás, versión 3.12.0, pero el proyecto ya se cataloga como inactivo.  

5. **Expects**:
    [Snyk Advisor](https://snyk.io/advisor/python/expects)  
    [PyPi](https://pypi.org/project/expects/)    
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación y además su última versión se publicó hace 2 años, 2 versiones de Python atrás, versión 3.11.0.  

6. **Ensure**:
    [Snyk Advisor](https://snyk.io/advisor/python/ensure)  
    [PyPi](https://pypi.org/project/ensure/)  
    Como podemos ver en su página de Snyk Advisor, tiene una baja puntuación, lo que nos lleva a la conclusión de no tenerla en cuenta. Sí es cierto que su última versión se publicó hace un año, 1 versión de Python atrás, versión 3.12.0, pero el proyecto ya se cataloga como inactivo.    

# Conclusión

Teniendo en cuenta los criterios formulados y las herramientas comparadas, las mejores opciones son Assert nativo de Python y Unittest, ya que son estándar en Python, ofrecen soporte activo y cumplen con los requisitos básicos de aserciones. Herramientas como Grappa, PyHamCrest, Expects y Ensure presentan desventajas significativas, como falta de actualizaciones recientes o baja puntuación en [Snyk Advisor](https://snyk.io/advisor/), lo que hace que las descarte. Finalmente, entre el Assert nativo de Python y Unittest tenemos que tener en cuenta que el segundo ofrece tipos de aserción, como podemos ver en la documentación oficial de Python [TestCase de Unittest](https://docs.python.org/es/3/library/unittest.html#unittest.TestCase). Por lo tanto, **Unittest** destaca como la opción más confiable y completa para este proyecto. Además, se usará el assert nativo de Python cuando sea posible. 

