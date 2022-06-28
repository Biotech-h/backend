import json
from http import HTTPStatus

from flask import Blueprint, abort, request

from backend.jobs_storage import JobStorage
from backend.errors import ConflictError
from backend.job_model import Job

storage = JobStorage()

routes = Blueprint('jobs', __name__)


@routes.get('/')
def get_all():
    return json.dumps(list(storage.get_all()))


@routes.get('/<int:uid>')
def get_by_id(uid):
    try:
        job = storage.get_by_id(uid)
    except ValueError as err:
        abort(HTTPStatus.NOT_FOUND, str(err))

    return job


@routes.delete('/<int:uid>')
def del_by_id(uid):
    try:
        storage.delete(uid)
    except ValueError as err:
        abort(HTTPStatus.NOT_FOUND, str(err))
    return {}, 204


@routes.put('/<int:uid>')
def change_job():
    payload = request.json
    new_job = Job(**payload)
    return storage.update(new_job.dict())


@routes.post('/')
def add():
    payload = request.json
    new_job = Job(**payload)
    return storage.add(new_job.dict())
