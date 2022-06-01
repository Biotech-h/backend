from flask import Flask
import json

app = Flask(__name__)

jobs = [{"name": "postdoctoral researcher"}]


@app.post('/api/jobs/')
def add_job():
    jobs.append({"name": "team leader"})
    return json.dumps(jobs)


if __name__ == "__main__":
    app.run(debug=True)
