install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml


.PHONY: install build publish package-install reinstall gendiff test lint selfcheck check