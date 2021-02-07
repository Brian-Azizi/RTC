test:
	behave

lint:
	mypy

format:
	black .

check-imports:
	autoflake -c --remove-unused-variables --remove-all-unused-imports --exclude book_files,virtualenv -r .

fix-imports:
	autoflake -i --remove-unused-variables --remove-all-unused-imports --exclude book_files,virtualenv -r .
