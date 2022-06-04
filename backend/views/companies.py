import json
from flask import Blueprint

routes = Blueprint('companies', __name__)

companies = [
    {'uid': 1, 'name': 'Moderna', 'region': 'USA', 'field': 'biotech'},
    {'uid': 2, 'name': 'Roche', 'region': 'Switzerland', 'field': 'biotech'}
]


@routes.get('/')
def get_all():
    return json.dumps(companies)


@routes.get('/<int:id>')
def get_company_by_id(id):
    for company in companies:
        if company['uid'] == id:
            return json.dumps(company)
    raise IndexError('Company not found')


@routes.delete('/<int:id>')
def del_company_by_id(id):
    for company in companies:
        if company['uid'] == id:
            del companies[companies.index(company)]
            return json.dumps(companies)
    raise IndexError('Company not found')