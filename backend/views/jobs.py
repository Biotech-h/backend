import json
import logging

from flask import Blueprint, request

from backend.job_model import CorrectJob
from backend.jobs_sqlstorage import JobsStorage

sql_storage = JobsStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('jobs', __name__)


@routes.get('/')
def get_all():
    logger.debug('request get all jobs')
    all_jobs = sql_storage.get_all()
    result = [CorrectJob.from_orm(jobs).dict() for jobs in all_jobs]

    return json.dumps(list(result))


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[job] get by id: %s', uid)
    job = sql_storage.get_by_id(uid)

    return CorrectJob.from_orm(job).dict()


@routes.delete('/<int:uid>')
def del_by_id(uid):
    logger.debug('[job] delete by id: %s', uid)
    sql_storage.delete(uid)

    return {}, 204


@routes.put('/<int:uid>')
def change_job(uid):
    logger.debug('[job] change by id: %s', uid)
    payload = request.json
    changed_job = CorrectJob(**payload)
    job = sql_storage.update(changed_job)

    return json.dumps(CorrectJob.from_orm(job).dict())


@routes.post('/')
def add():
    payload = request.json
    new_job = CorrectJob(**payload)
    job = sql_storage.add(new_job)

    return json.dumps(CorrectJob.from_orm(job).dict())
