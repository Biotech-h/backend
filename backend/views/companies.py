import json
from flask import Blueprint, abort

routes = Blueprint('companies', __name__)

companies = {
    1: {'name': 'Moderna', 'region': 'USA', 'field': 'biotech'},
    2: {'name': 'Roche', 'region': 'Switzerland', 'field': 'biotech'}
}


@routes.get('/')
def get_all():
    return json.dumps(companies)


@routes.get('/<int:uid>')
def get_by_id(uid):
    company = companies.get(uid)
    if company is None:
        abort(404, f"Unfortunately, company not found, uid: {uid}")
    return json.dumps(company)


@routes.delete('/<int:uid>')
def del_by_id(uid):
    company = companies.get(uid)
    if company is None:
        abort(404, f"Unfortunately, company not found, uid: {uid}")
    del companies[uid]
    return json.dumps(companies)