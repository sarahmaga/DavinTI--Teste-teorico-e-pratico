from models import db, Contact, Phone
from faker import Factory
from random import randint
from app import app
fake = Factory.create()
#Portugues
fake = Factory.create('pt_BR')
# Reload tables
with app.app_context():
    db.drop_all()
    db.create_all()
    # Make 5 fake contacts without alternative phones
    for num in range(5):
        name = fake.name()
        phone = fake.phone_number()
        age = randint(10,80)
        # Save in database
        my_contact = Contact(name=name, age=age)
        my_phone = Phone(phone_number=phone, contact = my_contact)
        print(my_contact.name,  my_phone.phone_number)
        db.session.add(my_phone)
        db.session.add(my_contact)
        
     # Make 5 fake contacts with alternative phones
    for num in range(5):
        name = fake.name()
        phone = fake.phone_number()
        phone2 = fake.phone_number()
        age = randint(10,80)
        # Save in database
        my_contact = Contact(name=name, age=age)
        my_phone = Phone(phone_number=phone, contact = my_contact)
        my_phone2 = Phone(phone_number=phone2, contact = my_contact)
        print(my_contact.name,  my_phone.phone_number)
        db.session.add(my_phone)
        db.session.add(my_phone2)
        db.session.add(my_contact)
        db.session.commit()
