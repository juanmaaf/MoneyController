.PHONY: install check clean test

install:
	uv lock

check:
	python3 -m py_compile money_controller/*.py

test: 
	uv run pytest