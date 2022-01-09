.PHONY: run migrate shell cov-html


run:
	source dev.env && poetry run ./manage.py runserver

migrate:
	source dev.env && poetry run ./manage.py migrate

shell:
	source dev.env && poetry run ./manage.py shell

cov-html:
	poetry run pytest --cov=hive --cov-report html tests/ && \
		open htmlcov/index.html