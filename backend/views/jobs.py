import json
import logging

from flask import Blueprint, request

from backend.schemas.job import CorrectJob
from backend.storages.jobs import JobsStorage

storage = JobsStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('jobs', __name__)


@routes.get('/')
def get_all():
    logger.debug('request get all jobs')
    entities = storage.get_all()
    jobs = [
        CorrectJob.from_orm(job).dict()
        for job in entities
    ]

    return json.dumps(list(jobs))


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[job] get by id: %s', uid)
    job = storage.get_by_id(uid)

    return CorrectJob.from_orm(job).dict()


@routes.delete('/<int:uid>')
def del_by_id(uid):
    logger.debug('[job] delete by id: %s', uid)
    storage.delete(uid)

    return {}, 204


@routes.put('/<int:uid>')
def change_job(uid):
    logger.debug('[job] change by id: %s', uid)
    payload = request.json
    changed_job = CorrectJob(**payload)
    job = storage.update(changed_job)

    return json.dumps(CorrectJob.from_orm(job).dict())


@routes.post('/')
def add():
    payload = request.json
    new_job = CorrectJob(**payload)
    job = storage.add(new_job)

    return json.dumps(CorrectJob.from_orm(job).dict())
