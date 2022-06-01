from flask import Flask
import json

app = Flask(__name__)

companies = [{'name': 'Pfizer'},
{'name': 'Novo Nordisk'}
]

@app.get('/api/companies/')
def get_all_companies():
    return json.dumps(companies)

if __name__ == "__main__":
    app.run(debug=True)