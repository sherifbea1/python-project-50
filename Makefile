lint:
	poetry run ruff check src tests --fix

test:
	PYTHONPATH=src poetry run pytest --cov=src tests/

