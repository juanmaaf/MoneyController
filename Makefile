.PHONY: install check clean

install:
	uv install

check:
	python -m py_compile money_controller/*.py
