import json
from flask import Blueprint, request

routes = Blueprint('jobs', __name__)

jobs = {
    1: {"title_job": "postdoctoral researcher",
        "description": "<str:description>"},
    2: {"title_job": "team leader",
        "description": "<str:description>"},
    3: {"title_job": "associate professor",
        "description": "<str:description>"}
}


@routes.get('/')
def get_all():
    return json.dumps(jobs)


@routes.get('/<int:uid>')
def get_by_id(uid):
    job = jobs.get(uid)
    return json.dumps(job)


@routes.delete('/<int:uid>')
def del_by_id(uid):
    del jobs[uid]
    return {}, 204


@routes.put('/<int:uid>')
def change_job(uid):
    jobs[uid] = request.json
    return jobs.get(uid)


@routes.post('/')
def add_job():
    payload = request.json
    jobs.append(payload)
    return payload
