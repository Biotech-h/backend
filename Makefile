-include .env
export

run:
	@python -m backend

lint:
	@mypy backend
	@flake8 backend

db.create:
	@python -m backend.database

db.makemigrations:
	@alembic revision --autogenerate -m "${message}"

db.migrate:
	@alembic upgrade head
