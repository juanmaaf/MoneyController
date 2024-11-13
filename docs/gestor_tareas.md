# Gestor de Tareas

Para automatizar tareas en este proyecto de Python, como ejecutar pruebas o verificar el estilo de código, he optado por **Poetry**. A continuación, explico las razones por las que `Poetry` es la opción más adecuada para este proyecto.  

## Razones para elegir Poetry como gestor de tareas

- **Integración con `pyproject.toml`**: Poetry permite centralizar las configuraciones y scripts de automatización directamente en el archivo `pyproject.toml`, lo que simplifica la administración del proyecto y evita la necesidad de archivos adicionales.  

- **Automatización de tareas**: Poetry permite definir y ejecutar comandos personalizados de manera sencilla, como ejecutar pruebas (`poetry run pytest`) o verificar el estilo de código (`poetry run flake8`). Esto elimina la necesidad de herramientas adicionales como `Make` o `Invoke`.  

- **Eficiencia en proyectos Python**: Al estar diseñado específicamente para trabajar con proyectos Python, Poetry optimiza el flujo de trabajo sin la necesidad de depender de herramientas externas o configuraciones adicionales.  

## Comparación con otras herramientas

- **Make**: Aunque `Make` es una herramienta poderosa y flexible, no está diseñada específicamente para proyectos Python, lo que implica la necesidad de crear y mantener un archivo `Makefile` adicional. Con Poetry, todas las tareas pueden centralizarse directamente en `pyproject.toml`, simplificando el proceso.  

- **Invoke**: Aunque `Invoke` es otro gestor de tareas popular en Python, añade una dependencia adicional que no es necesaria cuando se utiliza Poetry. Poetry cubre todas las necesidades de automatización de tareas para este proyecto de manera eficiente y directa.  

## Conclusión

**Poetry** es la opción ideal para la automatización de tareas en este proyecto, ya que permite gestionar tareas y comandos sin necesidad de herramientas adicionales, mejorando la eficiencia del flujo de trabajo y centralizando la configuración en un único archivo.  