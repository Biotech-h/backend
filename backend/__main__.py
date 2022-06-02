from flask import Flask, request
import json

app = Flask(__name__)

companies = [{'name': 'Pfizer'},
             {'name': 'Novo Nordisk'}
             ]

jobs = [{'name': 'postdoctoral researcher'}, {
    'name': 'team leader'}, {'name': 'associate professor'}
]


@app.get('/api/companies/')
def get_all_companies():
    return json.dumps(companies)


@app.get('/api/jobs/')
def get_all_jobs():
    return json.dumps(jobs)


@app.post('/api/jobs/')
def add_job():
    payload = request.json
    jobs.append(payload)
    return payload


if __name__ == "__main__":
    app.run(debug=True)
