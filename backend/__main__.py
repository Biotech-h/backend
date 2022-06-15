from flask import Flask
from backend.views import jobs
from backend.views import companies
from backend.errors import AppError
import logging

logging.basicConfig(level=logging.INFO)

def handle_app_errors(error: AppError):
    return {'error': error.reason}, error.status


app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')
app.register_blueprint(companies.routes, url_prefix='/api/v1/companies')
app.register_error_handler(AppError, handle_app_errors)

if __name__ == "__main__":
    app.run(debug=True)
