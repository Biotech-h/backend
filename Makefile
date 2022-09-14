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

migrate.upgrade:
	@alembic upgrade head

migrate.downgrade:
	@alembic downgrade ${message}
