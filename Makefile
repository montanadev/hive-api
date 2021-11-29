.PHONY: run migrate shell

run:
	DEBUG=true CORS_ORIGIN_WHITELIST=http://localhost:3000 SECRET_KEY=secret DATABASE_URL=sqlite:///sqlite.db && \
		poetry run ./manage.py runserver

migrate:
	DEBUG=true CORS_ORIGIN_WHITELIST=http://localhost:3000 SECRET_KEY=secret DATABASE_URL=sqlite:///sqlite.db && \
	 	poetry run ./manage.py migrate

shell:
	DEBUG=true CORS_ORIGIN_WHITELIST=http://localhost:3000 SECRET_KEY=secret DATABASE_URL=sqlite:///sqlite.db && \
		poetry run ./manage.py shell
