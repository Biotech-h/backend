import json
from flask import Blueprint, abort, request
from backend.companies_storage import CompaniesStorage

storage = CompaniesStorage()

routes = Blueprint('companies', __name__)


@routes.post('/')
def add():
    new_company = request.json
    try:
        company = storage.add(new_company)
    except ValueError as err:
        abort(409, str(err))

    return company


@routes.get('/')
def get_all():
    return json.dumps(list(storage.get_all()))


@routes.get('/<int:uid>')
def get_by_id(uid):
    try:
        company = storage.get_by_id(uid)
    except ValueError as err:
        abort(409, str(err))

    return company


@routes.delete('/<int:uid>')
def del_by_id(uid):
    try:
        storage.delete(uid)
    except ValueError as err:
        abort(409, str(err))

    return {}, 204


@routes.put('/<int:uid>')
def change_company(uid):
    new_company = request.json
    try:
        company = storage.update(new_company)
    except ValueError as err:
        abort(409, str(err))

    return company
