import logging

import orjson
from flask import Blueprint, request

from backend.schemas.company import CorrectCompany
from backend.schemas.job import CorrectJob
from backend.storages.companies import CompaniesStorage

storage = CompaniesStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('companies', __name__)


@routes.post('/')
def add():
    payload = request.json
    payload['uid'] = -1
    new_company = CorrectCompany(**payload)
    company = storage.add(new_company)

    return orjson.dumps(CorrectCompany.from_orm(company).dict())


@routes.get('/')
def get_all():
    logger.debug('request get all companies')
    entities = storage.get_all()
    companies = [
        CorrectCompany.from_orm(company).dict()
        for company in entities
    ]

    return orjson.dumps(list(companies))


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[company] get by id: %s', uid)
    company = storage.get_by_id(uid)

    return CorrectCompany.from_orm(company).dict()


@routes.delete('/<int:uid>')
def delete(uid):
    logger.debug('[company] delete by id: %s', uid)
    storage.delete(uid)

    return {}, 204


@routes.put('/<int:uid>')
def update(uid):
    logger.debug('[company] change by id: %s', uid)
    payload = request.json
    changed_company = CorrectCompany(**payload)
    company = storage.update(changed_company)

    return orjson.dumps(CorrectCompany.from_orm(company).dict())


@routes.get('<int:uid>/jobs/')
def get_jobs_by_company_uid(uid):
    logger.debug('[jobs] get by company id: %s', uid)
    entities = storage.get_jobs_by_company_id(uid)
    jobs = [
        CorrectJob.from_orm(job).dict()
        for job in entities
    ]

    return orjson.dumps(list(jobs))




#    jobs = storage.get_jobs_by_company_id(uid)

#   return orjson.dumps(list(jobs))
