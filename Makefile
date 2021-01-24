test:
	behave

lint:
	find . -type f -name "*.py" -not -path "./virtualenv/*" | xargs mypy

format:
	black .
