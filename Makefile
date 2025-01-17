.PHONY: install check

install:
	uv lock

check:
	python -m py_compile money_controller/*.py