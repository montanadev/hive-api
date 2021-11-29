.PHONY: run migrate shell

run:
	poetry run ./manage.py runserver

migrate:
	poetry run ./manage.py migrate

shell:
	poetry run ./manage.py shell
