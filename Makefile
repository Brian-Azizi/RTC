test:
	behave

lint:
	mypy

format:
	black .

ex-projectile:
	python -m examples.projectile
	open projectile.ppm