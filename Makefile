lint:
	poetry run flake8 src tests

test:
	PYTHONPATH=src poetry run pytest --cov=src tests/

