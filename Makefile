.PHONY: run migrate shell test-cov-html test

run:
	source dev.env && poetry run ./manage.py runserver

migrate:
	source dev.env && poetry run ./manage.py migrate

shell:
	source dev.env && poetry run ./manage.py shell

test:
	source dev.env && poetry run pytest --cov=hive

cov-html:
	source dev.env && poetry run pytest --cov=hive --cov-report html tests/ && \
		open htmlcov/index.html
