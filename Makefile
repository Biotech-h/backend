-include .env
export

run:
	@python -m backend

lint:
	@mypy backend
	@flake8 backend