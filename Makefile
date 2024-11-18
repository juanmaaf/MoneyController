# Definir los objetivos comunes como .PHONY para evitar conflictos con archivos
.PHONY: install check format lint style clean test build full clean-full

# Instalar dependencias usando Poetry
install:
	poetry install

# Verificar la configuración del proyecto con Poetry (asegura que no haya errores)
check:
	poetry check

# Formatear el código con Black
format:
	poetry run black .

# Comprobar la sintaxis con Flake8
lint:
	poetry run flake8 .

# Comprobar el estilo del código con Black
style:
	poetry run black --check .

# Limpiar archivos generados, como __pycache__ y archivos .pyc
clean:
	rm -rf *.pyc __pycache__

# Ejecutar pruebas con Pytest
test:
	poetry run pytest

# Construir el proyecto con Poetry
build:
	poetry build

# Ejecutar todas las tareas: formatear, verificar sintaxis, comprobar estilo, ejecutar pruebas y construir
full: format lint test build

# Limpiar y ejecutar todas las tareas anteriores: limpiar primero y luego hacer full
clean-full: clean full