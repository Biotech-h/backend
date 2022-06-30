import json
import logging

from flask import Blueprint, request

from backend.companies_sqlstorage import CompaniesStorage
from backend.company_model import CorrectCompany

sql_storage = CompaniesStorage()

logger = logging.getLogger(__name__)

routes = Blueprint('companies', __name__)


@routes.post('/')
def add():
    payload = request.json
    new_company = CorrectCompany(**payload)
    company = sql_storage.add(new_company)

    return json.dumps(CorrectCompany.from_orm(company).dict())


@routes.get('/')
def get_all():
    logger.debug('request get all companies')
    all_companies = sql_storage.get_all()
    result = [CorrectCompany.from_orm(companies).dict() for companies in all_companies]

    return json.dumps(list(result))


@routes.get('/<int:uid>')
def get_by_id(uid):
    logger.debug('[company] get by id: %s', uid)
    company = sql_storage.get_by_id(uid)

    return CorrectCompany.from_orm(company).dict()


@routes.delete('/<int:uid>')
def del_by_id(uid):
    logger.debug('[company] delete by id: %s', uid)
    sql_storage.delete(uid)

    return {}, 204


@routes.put('/<int:uid>')
def change_company(uid):
    logger.debug('[company] change by id: %s', uid)
    payload = request.json
    changed_company = CorrectCompany(**payload)
    company = sql_storage.update(changed_company)

    return json.dumps(CorrectCompany.from_orm(company).dict())
