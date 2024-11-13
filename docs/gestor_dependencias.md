# Gestor de Dependencias

Para la gestión de dependencias en este proyecto de Python, he optado por **Poetry**, un gestor moderno y ampliamente adoptado en la comunidad. A continuación, explico las razones por las que `Poetry` es la mejor opción para este proyecto.  

## Razones para elegir Poetry

- **Compatibilidad con `pyproject.toml`**: Poetry se basa en el estándar `pyproject.toml` para gestionar tanto las dependencias como la configuración del proyecto. Esto facilita su integración con herramientas y entornos modernos de Python.  
  
- **Control preciso de versiones de dependencias**: Con Poetry, se genera automáticamente un archivo `poetry.lock`, lo que garantiza la consistencia en las versiones de las dependencias entre distintos entornos, evitando así posibles conflictos.  
  
- **Gestión integrada de entornos virtuales**: Poetry facilita la creación y el manejo de entornos virtuales, lo que permite una clara separación entre proyectos y simplifica la instalación de dependencias.  
  
- **Actualización y gestión sencilla**: Con comandos como `poetry add` y `poetry update`, Poetry permite instalar nuevas dependencias y actualizar las existentes de manera eficiente, siempre asegurando la compatibilidad con las versiones más recientes.  

## Comparación con otras herramientas

- **PDM y Hatch**: Además de Poetry, existen otras herramientas que también soportan el estándar `pyproject.toml`, como **PDM** y **Hatch**. Sin embargo, Poetry sigue siendo la mejor opción por su simplicidad, facilidad de uso y sus funcionalidades integradas para el manejo de dependencias y entornos virtuales.  

## Conclusión

**Poetry** es la herramienta ideal para este proyecto gracias a su compatibilidad con `pyproject.toml`, su eficaz sistema de bloqueo de versiones y su capacidad para gestionar entornos virtuales de manera integrada.  