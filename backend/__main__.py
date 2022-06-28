from asyncio.log import logger
import logging

from pydantic import ValidationError
from backend.config import port, host

from flask import Flask

from backend.errors import AppError
from backend.views import companies, jobs

logging.basicConfig(level=logging.INFO)


def handle_app_errors(error: AppError):
    return {'error': error.reason}, error.status

def handle_validation_errors(error: ValidationError)
    logger.warning(str(error))
    return {'error': error.errors()}, 422


app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')
app.register_blueprint(companies.routes, url_prefix='/api/v1/companies')
app.register_error_handler(AppError, handle_app_errors)
app.register_error_handler(ValidationError, handle_validation_errors)

if __name__ == '__main__':
    app.run(host=host, port=port)
