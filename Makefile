.PHONY: install check

install:
	uv lock

check:
	python3 -m py_compile money_controller/*.py

test: 
	uv run pytest 
