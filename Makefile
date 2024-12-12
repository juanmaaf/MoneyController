.PHONY: install check clean

install:
	uv build && uv lock

check:
	python -m py_compile money_controller/*.py