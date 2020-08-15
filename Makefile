.PHONY: clean-pyc clean-build clean

PY = python3
PIP = pip3

help:
	@echo "clean - remove all build, pyc"
	@echo "clean-build - remove all build"
	@echo "clean-pyc - remove all python cache"
	@echo "dist - packaging"
	@echo "install - install by setup.py file local"
	@echo "release - packaging and upload as release"
	@echo "dev - install for development environment"

clean: clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

dist: clean
	${PY} setup.py sdist bdist_wheel
	ls -l dist/

release: clean
	${PY} setup.py sdist bdist_wheel
	twine upload dist/*

install: clean
	${PY} setup.py install

dev: clean
	pip install twine setuptools wheel
	${PIP} install --editable .
