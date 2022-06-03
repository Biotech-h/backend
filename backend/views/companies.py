import json
from flask import Blueprint

routes = Blueprint('companies', __name__)

companies = []

@routes.get('/')
def get_all():
    return json.dumps(companies)