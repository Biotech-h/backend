from flask import Flask
import json

app = Flask(__name__)

jobs = [{'name': 'postdoctoral researcher'}, {
    'name': 'team leader'}, {'name': 'associate professor'}
]


@app.get('/api/jobs')
def get_all_jobs():
    return json.dumps(jobs)


if __name__ == "__main__":
    app.run(debug=True)
