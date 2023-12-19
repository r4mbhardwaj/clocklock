.PHONY: install test pre-commit docs clean

install:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest --cov=clocklock --cov-report term-missing

fast-test:
	poetry run pytest --cov=clocklock --cov-report term-missing -n auto

linting:
	poetry run pre-commit run --all-files

docs:
	cd docs && poetry run make html

clean:
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .tox
	rm -rf src/*.egg-info
	find src tests -type f -name "*.py[co]" -delete
	find src tests -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf docs/build
	rm -rf dist
	rm -rf build

check: pre-commit test
