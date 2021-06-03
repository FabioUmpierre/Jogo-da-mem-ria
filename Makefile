VENV := .venv
PYTHON := $(VENV)/bin/python3

all: help

run:
	$(PYTHON) Jogo_da_Memoria.py

venv: 
	python3 -m venv $(VENV)

shell:
	source .venv/bin/activate

help:
	@echo "Help message"