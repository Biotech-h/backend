import logging
import os

from flask import Flask

from backend.errors import AppError
from backend.views import companies, jobs

logging.basicConfig(level=logging.INFO)


def handle_app_errors(error: AppError):
    return {'error': error.reason}, error.status


app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')
app.register_blueprint(companies.routes, url_prefix='/api/v1/companies')
app.register_error_handler(AppError, handle_app_errors)

host = os.environ['HOST']
port = os.environ['PORT']

if __name__ == '__main__':
    app.run(host=host, port=port)
