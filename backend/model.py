from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Company(db.Model):
    id: db.Column(db.Integer, primary_key=True)
    name: db.Column(db.String, nullable=False)
    region: db.Column(db.String, nullable=False)
    category: db.Column(db.String, nullable=False)
    description: db.Column(db.Text, nullable=False)
