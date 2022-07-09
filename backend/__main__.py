import logging

from flask import Flask
from pydantic import ValidationError

from backend.config import host, port
from backend.database.db import db_session
from backend.errors import AppError
from backend.views import companies, jobs

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def handle_app_errors(error: AppError):
    logger.warning(error)
    return {'error': error.reason}, error.status


def handle_validation_errors(error: ValidationError):
    logger.warning(error)
    return {'error': error.errors()}, 422


def shutdown_session(exception=None):
    db_session.remove()


app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')
app.register_blueprint(companies.routes, url_prefix='/api/v1/companies')
app.register_error_handler(AppError, handle_app_errors)
app.register_error_handler(ValidationError, handle_validation_errors)

app.teardown_appcontext(shutdown_session)

if __name__ == '__main__':
    app.run(host=host, port=port)
