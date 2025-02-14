install:
	uv sync --frozen

fix:
	ruff check --fix-only

lint:
	ruff check
	mypy .

format:
	ruff format

test:
	python -m unittest discover tests
