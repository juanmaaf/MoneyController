# Elección de Herramienta CI  

Para poder añadir integración continua al proyecto que se desarrolla en este repositorio, el primer paso es elegir la herramienta CI que se va a emplear. Para la búsqueda de herramientas, he buscado en foros de Reddit como [¿Qué herramienta de CI/CD utiliza?](https://www.reddit.com/r/devops/comments/1hm24sj/which_cicd_tool_do_you_use/?tl=es-es&rdt=51106) o [¿En qué herramienta de CI/CD vale la pena invertir mi tiempo?](https://www.reddit.com/r/devops/comments/12ekx2i/which_cicd_tool_is_the_most_worthy_to_invest_my/?tl=es-es) y páginas buscando Herramientas CI directament en el navegador como [Herramientas de integración continua](https://www.atlassian.com/es/continuous-delivery/continuous-integration/tools). Además, también he tenido en cuenta las herramientas mencionadas en el guion. A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto.   

## Criterios de Selección  

1. La herramienta debe ser un servicio gratuito (freemium). Es un requisito mínimo.    
2. La herramienta debe poder conectarse al repositorio GitHub a través del REST API para checks [REST API GitHub](https://docs.github.com/en/rest/checks?apiVersion=2022-11-28). Es un requisito mínimo.    

## Comparación de Herramientas  

1. **GitHub Actions**:  
    [GitHub Actions](https://github.com/features/actions)  
    Esta herramienta es gratis para los repositorios públicos de GitHub y tiene un límite gratuito de 2000 minutos mensuales para repositorios privados. Puede conectarse al respositorio GitHub ya que es una herramienta integrada en GitHub.  

2. **Circle CI**:  
    [Circle CI](https://circleci.com/)  
    Esta herramienta ofrece un plan gratuito con un límite de 6000 minutos mensuales. Puede conectarse al repositorio de GitHub creando una cuenta en su página web y accediendo a las funcionalidades que ofrece. Es necesario definir un archivo `.circleci/config.yml` en este repositorio.  

3. **Semaphore CI**:  
    [Semaphore CI](https://semaphoreci.com/)    
    Esta herramienta ofrece un plan gratuito con un límite de 7000 minutos mensuales. Puede conectarse al repositorio de GitHub iniciando sesión con GitHub en su página web. Es necesario definir un archivo `.semaphore/semaphore.yml` en este repositorio.  

4. **Travis CI**:
    [Travis CI](https://www.travis-ci.com/)  
    Esta herramienta ofrece las primeras 100 builds gratis pero luego exige un pago mínimo mensual de 13.75$. Se descarta esta herramienta por no ser un servicio gratuito.  

5. **Appveyor**:
    [Appveyor](https://www.appveyor.com/)  
    Esta herramienta es gratis para los repositorios públicos. Puede conectarse al repositorio de GitHub iniciando sesión con GitHub en su página web. Es necesario definir un archivo `appveyor.yml` en este repositorio.  


## Conclusión  

GitHub Actions, Circle CI, Semaphore CI y Appveyor son las herramientas que cumplen los criterios establecidos. Según el guion, debemos examinar varios sistemas de integración continua, por lo que se van a examinar y configurar los 4 mencionados.

- En primer lugar, **GitHub Actions**. Es necesario definir un archivo dentro del directorio `.github/workflows/` al que llamaremos `ci.yml`. En cuanto a las versiones de Python que se testean, he elegido Python 3.13 debido a que es la versión requerida por el proyecto, según el archivo `pyproject.toml`. Además, se ha testeado Python 3.10, ya que es una versión estable y ampliamente adoptada, que sigue siendo compatible con muchas configuraciones de producción y tiene soporte a largo plazo.    
- En segundo lugar, **Circle CI**. Es necesario definir un archivo `config.yml` dentro de un directorio que también debe crearse llamado `.circleci`.
- En tercer lugar, **Semaphore CI**. Es necesario definir un archivo `semaphore.yml` dentro de un directorio que también debe crearse llamado `.semaphore`.
- Por último, **Appveyor**. Es necesario definir un archivo `appveyor.yml` en la raíz del proyecto que se desarrolla en este repositorio.   