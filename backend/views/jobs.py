import json
from flask import Blueprint, request

routes = Blueprint('jobs', __name__)

jobs = []


@routes.get('/')
def get_all():
    return json.dumps(jobs)


@routes.post('/')
def add_job():
    payload = request.json
    jobs.append(payload)
    return payload
