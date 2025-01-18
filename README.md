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

## Biblioteca de Aserciones y Test Runner

- Biblioteca de aserciones: `Unittest`. [Más información](/docs/biblioteca_aserciones.md)

- Test Runner: `Pytest`. [Más información](/docs/test_runner.md)  

- Herramienta CLI para ejecutar test: `Pytest`. [Más información](/docs/herramientas_cli.md)  

# Herramientas utilizadas

- Lenguaje de programación: `Python`

- Gestor de Dependencias: `UV`. [Más información](/docs/gestor_dependencias.md)

- Gestor de Tareas: `Make`. [Más información](/docs/gestor_tareas.md)
    
    - Para instalar las dependencias del proyecto realizamos: `make install`

    - Para verificar que el código compila correctamente:
    `make check`

    - Para ejecutar los test realizamos:
    `make test`

## Datos del Usuario 

El usuario dispone de un archivo csv, descargado de su aplicación del banco, donde pueden verse los distintos ingresos y gastos listados por fecha. Los atributos que proporciona el banco son 5 (Fecha,Concepto,Categoría,Importe,Tipo Movimiento). Como podemos ver, hay gastos que podemos identificar gracias a los atributos Concepto y Categoría. La gestión de los Bizum (categoría Transferencias) es más difícil de identificar, ya que el usuario puede no recordar qué son esos Bizum enviados y recibidos, pero el banco dispone del concepto asociado al Bizum. Dado que en este proyecto se van a gestionar los gastos, para identificar los Bizum, se incluirá el concepto que proporciona el banco asociado a la Transferencia.

[CSV con los Datos del Usuario](/docs/gastos.csv)
