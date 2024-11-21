# Definir los objetivos comunes como .PHONY para evitar conflictos con archivos
.PHONY: install check clean

# Instalar dependencias usando Poetry
install:
	uv install

# Verificar si el código compila correctamente
check:
	python -m py_compile money_controller/*.py

# Limpiar archivos temporales generados
clean:
	rm -rf *.pyc __pycache__  