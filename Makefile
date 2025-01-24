.PHONY: install check test

install-uv:
	wget -qO- https://astral.sh/uv/install.sh | sh

install:
	uv lock

check:
	python3 -m py_compile money_controller/*.py

test: 
	uv run pytest 
