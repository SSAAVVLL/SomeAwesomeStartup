from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=True)

    def to_dict(self):
        return {column.key: getattr(self, attr) for attr, column in self.__mapper__.c.items()}

    def __repr__(self):
        return f"Contact({self.firstname}, {self.lastname}, {self.phone})"
