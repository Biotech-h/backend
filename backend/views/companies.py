import json

from flask import Blueprint, abort, request

from backend.sql_storage import CompaniesStorage
from backend.errors import ConflictError, NotFoundError
from backend.companies_model import CorrectCompany

import logging


sql_storage = CompaniesStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('companies', __name__)


@routes.post('/')
def add():
    payload = request.json
    new_company = CorrectCompany(**payload)
    try:
        company = sql_storage.add(new_company)
    except ConflictError as err:
        abort(409, str(err))

    return json.dumps(CorrectCompany.from_orm(company).dict())


@routes.get('/')
def get_all():
    logger.debug('request get all companies')
    all_companies = sql_storage.get_all()
    return json.dumps(CorrectCompany.from_orm(companies).dict() for companies in all_companies)


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[company] get by id: %s', uid)
    try:
        company = sql_storage.get_by_id(uid)
    except NotFoundError as err:
        abort(404, str(err))

    return CorrectCompany.from_orm(company).dict()


@routes.delete('/<int:uid>')
def del_by_id(uid):
    logger.debug('[company] delete by id: %s', uid)
    try:
        sql_storage.delete(uid)
    except NotFoundError as err:
        abort(404, str(err))

    return {}, 204


@routes.put('/<int:uid>')
def change_company(uid):
    logger.debug('[company] change by id: %s', uid)
    payload = request.json
    changed_company = CorrectCompany(**payload)
    try:
        company = sql_storage.update(changed_company)
    except NotFoundError as err:
        abort(404, str(err))

    return json.dumps(CorrectCompany.from_orm(company).dict())
