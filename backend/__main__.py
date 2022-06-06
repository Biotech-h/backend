from flask import Flask
from backend.views import jobs
from backend.views import companies

app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')
app.register_blueprint(companies.routes, url_prefix='/api/v1/companies')

if __name__ == "__main__":
    app.run(debug=True)
