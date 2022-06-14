import json
from flask import Blueprint, abort, request
from backend.companies_storage import CompaniesStorage
from backend.errors import ConflictError, NotFoundError
from backend.companies_model import CorrectCompany
import logging

storage = CompaniesStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('companies', __name__)


@routes.post('/')
def add():
    payload = request.json
    new_company = CorrectCompany(**payload)
    try:
        company = storage.add(new_company.dict())
    except ConflictError as err:
        abort(409, str(err))

    return company


@routes.get('/')
def get_all():
    logger.debug('request get all companies')
    return json.dumps(list(storage.get_all()))


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[company] get by id: %s', uid)
    try:
        company = storage.get_by_id(uid)
    except NotFoundError as err:
        abort(404, str(err))

    return company


@routes.delete('/<int:uid>')
def del_by_id(uid):
    logger.debug('[company] delete by id: %s', uid)
    try:
        storage.delete(uid)
    except NotFoundError as err:
        abort(404, str(err))

    return {}, 204


@routes.put('/<int:uid>')
def change_company(uid):
    logger.debug('[company] change by id: %s', uid)
    payload = request.json
    changed_company = CorrectCompany(**payload)
    try:
        company = storage.update(changed_company.dict())
    except NotFoundError as err:
        abort(404, str(err))

    return company
