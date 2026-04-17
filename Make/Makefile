SHELL := /bin/bash

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip
RUFF := $(PYTHON) -m ruff
MYPY := $(PYTHON) -m mypy
PYTEST := $(PYTHON) -m pytest

.DEFAULT_GOAL := help

.PHONY: help venv install run format lint typecheck check-requirements test docs build check clean

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

$(PYTHON):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

venv: $(PYTHON) ## Create the local virtual environment

install: $(PYTHON) requirements-dev.txt ## Install runtime and development dependencies into .venv
	$(PIP) install -r requirements-dev.txt

run: install ## Run the demo application with the project interpreter
	PYTHONPATH=src $(PYTHON) -m demo_app.app

format: install ## Reformat the codebase
	$(RUFF) format src tests scripts

lint: install ## Check formatting and style without changing files
	$(RUFF) check src tests scripts
	$(RUFF) format --check src tests scripts

typecheck: install ## Run static type checks
	MYPYPATH=src $(MYPY) src tests

check-requirements: install ## Compare imported modules with requirements.txt
	PYTHONPATH=src $(PYTHON) scripts/check_requirements.py --source-dir src --requirements requirements.txt

test: install ## Run the automated test suite
	PYTHONPATH=src $(PYTEST) -q

docs: install ## Build a small documentation artifact that summarizes the project setup
	$(PYTHON) scripts/build_report.py

build: install ## Build an executable zipapp artifact
	mkdir -p build
	$(PYTHON) -m zipapp src -m "demo_app.app:main" -o build/demo_app.pyz

check: lint typecheck check-requirements test ## Run all quality gates

clean: ## Remove generated artifacts and local virtual environment
	rm -rf $(VENV) .mypy_cache .pytest_cache .ruff_cache build
