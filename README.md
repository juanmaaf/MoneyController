# MoneyController
Repositorio para el proyecto de Infraestructura Virtual.

## Problema a Resolver
### Formulación del Problema 
Un alumno de Ingeniería Informática tiene problemas de presupuesto, ya que no consigue llegar a final de mes económicamente. Cada mes tiene unos gastos esenciales que cubrir, como alquiler, comunidad de vecinos e internet. Además, debe cubrir otros gastos que varían a lo largo del tiempo, como compras o facturas (electricidad, agua, gas). Además, destina parte de su presupuesto a ahorro. 

El estudiante tiene acceso a datos financieros en formato digital, descargando su estado bancario, pero tiene dificultades en el análisis de los mismos para poder tomar decisiones informadas. Actualmente, no cuenta con una herramienta con una herramienta que le permita categorizar sus gastos o calcular cuánto puede gastar un determinado día sin comprometer sus necesidades esenciales ni sus metas de ahorro. Le gustaría una solución que le facilitase esta tarea, sin tener que analizar detalladamente cada uno de los gastos empleando demasiado tiempo en ello.  

## Desarrollo del Proyecto
### Historias de Usuario
Se han definido las siguientes historias de usuario: 
1. [HU1] - Falta de Control sobre los Gastos  
2. [HU2] - Falta de Información para Decidir si un Gasto Adicional es Viable

[Historias de Usuario](/docs/historias_usuario.md)  

### User Journeys
Se han definido los siguientes user journeys:
1. [UserJourney1] - Registro de Gastos  
3. [UserJourney2] - Evaluación de Gasto Adicional  

[User Journeys](/docs/user_journeys.md)  

### Milestones
Se han definido los siguientes milestones:
1. [M0] - Modelo del Problema
2. [M1] - Algoritmo de Gastos 

[Milestones](/docs/milestones.md)  

# Herramientas utilizadas

- Lenguaje de programación: `Python`

- Gestor de dependencias: `Poetry`. [Más información](/docs/gestor_dependencias.md)

- Gestor de tareas: `Poetry` (utilizado también como gestor de tareas). [Más información](/docs/gestor_tareas.md)
    - Si no está instalado, su instalación es muy simple y basta con ejecutar el siguiente comando:
    `curl -sSL https://install.python-poetry.org | python3 -`
    
    - Para instalar las dependencias del proyecto realizamos:
    `poetry install`

    - Para formatear el código y corregir la sintaxis (utilizando `black`) realizamos:
    `poetry run format_code`

    - Para comprobar la sintaxis de los archivos (utilizando `flake8` en este caso) realizamos:
    `poetry run check_syntax`

    - Para comprobar el estilo del código (utilizando `black`) realizamos:
    `poetry run check_style`

    - Para limpiar los archivos generados en la construcción del proyecto (eliminando entornos virtuales y archivos temporales) realizamos:
    `poetry run clean`

    - Para ejecutar las pruebas (utilizando `pytest`) realizamos:
    `poetry run test`

    - Para construir el proyecto (por ejemplo, empaquetarlo para distribución) realizamos:
    `poetry run build`

    - Con `poetry run full` corregimos la sintaxis, verificamos el estilo, compilamos el proyecto y ejecutamos las pruebas.

    - Con `poetry run clean-full` realizamos todo lo anterior, pero primero limpiamos los archivos de compilación.
