# Elección de Herramienta CI  

Para poder añadir integración continua al proyecto que se desarrolla en este repositorio, el primer paso es elegir la herramienta CI que se va a emplear. Para la búsqueda de herramientas, he buscado en foros de Reddit como [¿Qué herramienta de CI/CD utiliza?](https://www.reddit.com/r/devops/comments/1hm24sj/which_cicd_tool_do_you_use/?tl=es-es&rdt=51106) o [¿En qué herramienta de CI/CD vale la pena invertir mi tiempo?](https://www.reddit.com/r/devops/comments/12ekx2i/which_cicd_tool_is_the_most_worthy_to_invest_my/?tl=es-es) y páginas buscando Herramientas CI directament en el navegador como [Herramientas de integración continua](https://www.atlassian.com/es/continuous-delivery/continuous-integration/tools). Además, también he tenido en cuenta las herramientas mencionadas en el guion. A continuación, detallo los criterios específicos establecidos antes de realizar la elección, para luego seleccionar la herramienta que mejor se ajusta a los objetivos del proyecto.   

## Criterios de Selección  

1. La herramienta debe ser un servicio gratuito (freemium) 
2. La herramienta debe poder conectarse al repositorio GitHub.  
3. Intentar minimizar las dependencias. Se considerarán las herramientas que no añadan dependencias al proyecto.   

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

4. **Jenkins**:  
    [Jenkins](https://www.jenkins.io/)  
    Para poder usar esta herramienta, necesitamos descargarla desde su página Web [Jenkins Download](https://www.jenkins.io/download/). Se descarta esta herramienta por añadir dependencias al proyecto.   

5. **Travis CI**:
    [Travis CI](https://www.travis-ci.com/)  
    Esta herramienta ofrece las primeras 100 builds gratis pero luego exige un pago mínimo mensual de 13.75$. Se descarta esta herramienta por no ser un servicio gratuito.  

6. **Appveyor**:
    [Appveyor](https://www.appveyor.com/)  
    Esta herramienta es gratis para los repositorios públicos. Puede conectarse al repositorio de GitHub iniciando sesión con GitHub en su página web. Es necesario definir un archivo `appveyor.yml` en este repositorio.  


## Conclusión  