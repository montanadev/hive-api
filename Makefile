.PHONY: run migrate shell


run:
	source dev.env && poetry run ./manage.py runserver

migrate:
	source dev.env && poetry run ./manage.py migrate

shell:
	source dev.env && poetry run ./manage.py shell
