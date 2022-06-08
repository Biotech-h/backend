import json
from flask import Blueprint, abort, request
from backend.companies_storage import CompanyStorage

storage = CompanyStorage()

routes = Blueprint('companies', __name__)


@routes.get('/')
def get_all():
    return json.dumps(storage.get_all)


@routes.get('/<int:uid>')
def get_by_id(uid):
    company = storage.get_by_id
    if company is None:
        abort(404, f"Unfortunately, company not found, uid: {uid}")
    return json.dumps(company)


@routes.delete('/<int:uid>')
def del_by_id(uid):
    storage.delete
    return json.dumps(storage.get_all)


@routes.put('/<int:uid>')
def change_company(uid):
    new_company = request.json
    storage.update(new_company)
    return json.dumps(CompanyStorage.get_all)

