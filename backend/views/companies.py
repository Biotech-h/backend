import json
from flask import Blueprint, abort, request
from companies_storage import CompanyStorage

routes = Blueprint('companies', __name__)


@routes.get('/')
def get_all():
    return json.dumps(CompanyStorage.get_all)


@routes.get('/<int:uid>')
def get_by_id(uid):
    company = CompanyStorage.get_by_id
    if company is None:
        abort(404, f"Unfortunately, company not found, uid: {uid}")
    return json.dumps(company)


@routes.delete('/<int:uid>')
def del_by_id(uid):
    CompanyStorage.delete
    return json.dumps(CompanyStorage.get_all)


@routes.put('/<int:uid>')
def change_company(uid):
    new_company = request.json
    CompanyStorage.update(new_company)
    return json.dumps(CompanyStorage.get_all)

