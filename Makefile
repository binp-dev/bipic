.DEFAULT_GOAL := help
.PHONY: deps lint format help

REPO_ROOT:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

deps: ## install deps (library & development)
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

lint: ## run linters, formatters for current python versions
	python3 -m flake8 bipic
	python3 -m pylint bipic

format: ## autoformat code with black and isort
	python3 -m isort bipic setup.py
	python3 -m black bipic setup.py

help: ## Show help message
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done