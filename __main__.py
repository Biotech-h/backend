from flask import Flask

app = Flask(__name__)

companies = [{'name': 'Pfizer'},
{'name': 'Novo Nordisk'}
]

@app.get('/api/companies/')
def get_all_companies():
    return companies

if __name__ == "__main__":
    app.run(debug=True)