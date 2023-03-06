from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Contacts table
class Contact(db.Model):


    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column (db.Integer, nullable = True)
    phones = db.relationship('Phone', backref='contact')
    def __repr__(self):
        return '<Contact %r>' % self.name

# Phone table
class Phone(db.Model):


    __tablename__ = 'phones'

    id_contact = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(16), nullable=True, unique=False)
    def __repr__(self):
        return '<Phone %r>' % self.phone_number
    


  

