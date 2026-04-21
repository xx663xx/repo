PYTHON = python3
VENV = .venv
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
MYPY = $(VENV)/bin/mypy
RUFF = $(VENV)/bin/ruff
TWINE = $(VENV)/bin/twine
VENV_PYTHON = $(VENV)/bin/python

.PHONY: venv install lint type test docs build check clean publish-testpypi

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

lint:
	$(RUFF) check src tests

type:
	$(MYPY) src

test:
	$(PYTEST)

docs:
	mkdir -p site
	cp README.md site/index.md

build:
	$(VENV_PYTHON) -m build --no-isolation

check: lint type test docs build

publish-testpypi: build
	$(TWINE) upload --repository testpypi dist/*

clean:
	rm -rf build dist site .pytest_cache .mypy_cache .ruff_cache src/*.egg-info
