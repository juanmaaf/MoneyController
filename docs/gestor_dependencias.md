# Gestor de Dependencias
En el desarrollo del anterior objetivo, se usó el archivo `pyproject.toml` como archivo de configuración del proyecto para poder seguir las buenas prácticas del lenguaje. Usar este archivo sigue las buenas prácticas del leguaje ya que desde las siguientes Propuestas de Mejora de Python (PEP) se llega al acuerdo de usarlo: [PEP 517](https://peps.python.org/pep-0517/) y el [PEP 518](https://peps.python.org/pep-0518/).

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles.  Aquí detallo los criterios específicos que se establecieron antes de realizar la elección, para luego seleccionar la herramienta que mejor cumple con los objetivos del proyecto.  

- La herramienta elegida como gestor de dependencias debe usar `pyproject.toml` como archivo de configuración, facilitando la centralización y estandarización de las dependencias del proyecto. Es un requisito mínimo que permite cumplir con las buenas prácticas mencionadas al principio.    
- Se considerará la puntuación de [Snyk Advisor](https://snyk.io/advisor/). Esta puntuación está basada en cuatro distintos criterios (Security, Popularity, Maintenance y Community). Esta puntuación nos permite comparar las herramientas de forma objetiva. 
- Se considerará que la herramienta sea lo más rápida posible para instalar dependencias de manera eficiente y con un impacto mínimo en el flujo de desarrollo. Podemos verificar de forma objetiva este criterio basándonos en la información proporcionada por Astral [Astral](https://astral.sh/blog/uv), comparando las herramientas que se comparan a continuación. 

## Comparación de Herramientas

Para gestionar dependencias en este proyecto, se evaluaron cuatro herramientas: Poetry, PDM, Hatch y UV. La comparación se basa en los criterios específicos establecidos.  

1. **Poetry**: 
   [Poetry](https://github.com/python-poetry/poetry)    
   [Poetry Snyk](https://snyk.io/advisor/python/poetry)  
   Poetry es una herramienta bastante popular y conocida basada en `pyproject.toml` para la gestión de dependencias. Como podemos ver en su página de Snyk, tiene una alta puntuación (94/100). A pesar de tener su última versión publicada hace 2 días, el criterio "Maintenance" está catalogado como "Sustainable". 

2. **PDM**:  
   [PDM](https://github.com/pdm-project/pdm)   
   [PDM Snyk](https://snyk.io/advisor/python/pdm)     
   PDM es una herramienta moderna basada en `pyproject.toml` para la gestión de depencencias. Como podemos ver en su página de Snyk, tiene una alta puntuación (94/100), igual que Poetry. Sin embargo, a diferencia de poetry, el criterio "Maintenance" está catalogado como "Healthy".

3. **Hatch**: 
   [Hatch](https://github.com/pypa/hatch)  
   [Hatch Snyk](https://snyk.io/advisor/python/hatch)  
   Hatch es una herramienta moderna basada en `pyproject.toml` para la gestión de depencencias. Como podemos ver en su página de Snyk, tiene una puntuación media-alta (85/100), menor que Poetry y PDM. Igual que Poetry, el criterio "Maintenance" está catalogado como "Sustainable" a pesar de tener una últma versión publicada hace 29 días. 

4. **UV**: 
   [UV](https://github.com/astral-sh/uv)   
   [UV Snyk](https://snyk.io/advisor/python/uv)  
   UV es una herramienta emergente enfocada en la velocidad. Tanto en su página de GitHub como Snyk, podemos ver que es extremadamente rápida en comparación a Poetry y PDM, como se puede ver en la gráfica proporcionada. Está basada en `pyproject.toml`. Como podemos ver en su página de Snyk, tiene una puntuación alta (93/100), similar a PDM y Poetry. Igual que PDM, el criterio "Maintenance" está catalogado como "Healthy", y su última versión fue publicada hace 2 días. 

## Conclusión

Las 4 herramientas se basan en `pyproject.toml` para la gestión de dependencias, y tienen una alta puntuación en Snyk, que evalúa los cuatro criterios mencionados. En primer lugar descarto Hatch, al ser la herramienta con menor puntuación en Snyk además de tener el criterio "Maintenance" catalogado como "Sustainable". Entre PDM, Poetry y UV se podría elegir cualquiera de las herramientas, ya que cumplen con los criterios especificados y además tienen una puntuación similar en Snyk. Sin embargo, el criterio referente a la velocidad de la herramienta, me permite diferenciar estas tres herramientas con objetividad, basándome en la gráfica que compara las herramientas proporcionada por [Astral](https://astral.sh/blog/uv). También podemos ver esta gráfica en las páginas de Snyk y GitHub de UV, midiendo el tiempo que tarda cada una de las herramientas. Por tanto, elijo **UV** como gestor de dependencias para el proyecto de este repositorio. 
