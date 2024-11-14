# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he evaluado las opciones disponibles y he optado por **Poetry**. Basé mi selección en los siguientes criterios específicos que necesita el proyecto:  

- **Control de versiones preciso y reproducibilidad**: El proyecto requiere consistencia en las versiones de dependencias para evitar conflictos en distintos entornos.  
- **Gestión de entornos virtuales integrada**: Necesitamos que el gestor permita crear y manejar entornos virtuales sin necesidad de herramientas adicionales.  
- **Centralización de configuraciones**: Dado que la configuración de dependencias y del proyecto debe estar en un solo archivo, preferimos herramientas compatibles con el estándar `pyproject.toml`.  

## Razones para elegir Poetry

- **Control de versiones preciso**: `Poetry` genera automáticamente un archivo `poetry.lock`, lo cual garantiza que cada colaborador utilice exactamente las mismas versiones de dependencias, evitando conflictos entre entornos.  
- **Gestión de entornos virtuales**: `Poetry` facilita la creación y el manejo de entornos virtuales, lo cual asegura una separación limpia entre proyectos.  
- **Compatibilidad con `pyproject.toml`**: Al utilizar `pyproject.toml` como archivo de configuración central, `Poetry` simplifica la administración del proyecto y evita la necesidad de otros archivos.   

## Comparación con otras herramientas

- **PDM y Hatch**: Además de Poetry, existen otras herramientas que también soportan el estándar `pyproject.toml`, como **PDM** y **Hatch**. Sin embargo, Poetry sigue siendo la mejor opción por su simplicidad, facilidad de uso y sus funcionalidades integradas para el manejo de dependencias y entornos virtuales.  

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su eficaz sistema de bloqueo de versiones y su capacidad para gestionar entornos virtuales de manera integrada.  