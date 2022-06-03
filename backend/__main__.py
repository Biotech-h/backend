import json
from flask import Flask, request
from backend.views import jobs

app = Flask(__name__)
app.register_blueprint(jobs.routes, url_prefix='/api/v1/jobs')

companies = [{'name': 'Pfizer'},
             {'name': 'Novo Nordisk'}
             ]


@app.get('/api/companies/')
def get_all_companies():
    return json.dumps(companies)


if __name__ == "__main__":
    app.run(debug=True)
