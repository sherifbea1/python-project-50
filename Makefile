lint:
	uv run ruff check src tests --fix

test:
	PYTHONPATH=src uv run pytest --cov=src tests/