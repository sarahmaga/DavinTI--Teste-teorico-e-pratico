from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Contact, Phone
from forms import ContactForm
import traceback
import time
# Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = False

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('contacts'))


@app.route("/new_contact", methods=('GET', 'POST'))
def new_contact():
    '''
    Create new contact
    '''
    form = ContactForm()
    if form.validate_on_submit(): 
        # Creating main phone number object
        my_contact = Contact(name = form.name.data, age = form.age.data)
        phone1 = Phone (phone_number = form.phone.data, contact = my_contact )

        phone2 = Phone()
        # If there is an alternative phone number
        if form.phone2.data != None:
            phone2  = Phone (phone_number = form.phone2.data, contact = my_contact )
        
        db.session.add(my_contact)
        db.session.add(phone1)
        if phone2 != None:
            db.session.add(phone2)

        try:
            db.session.commit()
            # User info
            flash('Contato criado corretamente', 'success')
            return redirect(url_for('contacts'))
        except :
            print(traceback.print_exc())
            db.session.rollback()
            flash('Erro ao criar contato.', 'danger')

    contacts1 = Contact.query.all()
    for contacts2 in contacts1:
      print ("Nome---->",contacts2.name)
      for phones in contacts2.phones:
        print("Telefone------>",phones.phone_number)
    return render_template('web/new_contact.html', form=form)


@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    '''
    Edit contact

    :param id: Id from contact
    '''
    my_contact = Contact.query.filter_by(id=id).first()
    lista = []
    possible_phones = Phone.query.all()
    for i in possible_phones:
        aux1 = int(id)
        aux2 = int(i.id_contact)
        if aux1== aux2:
            lista.append(i)
    
    form = ContactForm(name = my_contact.name, phone = lista[0].phone_number,  age = my_contact.age)

    if len(lista) == 2:
        form = ContactForm(name = my_contact.name, phone = lista[0].phone_number,phone2 = lista[1].phone_number,  age = my_contact.age)
        lista[1].phone_number = form.phone2.data
        db.session.add(lista[1])

    if form.validate_on_submit():
        try:
            # Update contact
            my_contact.name = form.name.data 
            lista[0].phone_number = form.phone.data
            my_contact.age = form.age.data 
            db.session.add(my_contact)
            db.session.add(lista[0])
            db.session.commit()
            # User info
            flash('Salvo com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Erro ao salvar contato.', 'danger')
    return render_template(
        'web/edit_contact.html',
        form=form)


@app.route("/contacts")
def contacts():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts = contacts )


@app.route("/search")
def search():
    '''
    Search
    '''
    # Replacing nom number characters
    name_search = request.args.get('name')
    name_search_clean = name_search.replace(" ","")
    name_search_clean = name_search.replace("+","")
    name_search_clean = name_search.replace("(","")
    name_search_clean = name_search.replace(")","")
    aux = []
    all_contacts = Contact()
    # Search for name
    if name_search_clean.isdigit() == False:
        aux = Contact.query.filter(
            Contact.name.contains(name_search)
            ).order_by(Contact.name).all()
        
    # Search for phone number
    else: 
        all_phones = Phone.query.filter(
            Phone.phone_number.contains(name_search)
            ).order_by(Phone.id).all()
        
        for i in all_phones:
            all_contacts = Contact.query.get(i.id_contact)
            aux.append(all_contacts)

    return render_template('web/contacts.html', contacts=aux)


@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    '''
    Delete contact
    '''
    try:
        my_contact = Contact.query.filter_by(id=request.form['id']).first()
        lista = []
        possible_phones = Phone.query.all()
        for i in possible_phones:
            aux1 = int(my_contact.id)
            aux2 = int(i.id_contact)
            if aux1== aux2:
                lista.append(i)
        for i in lista:
            db.session.delete(i)
        db.session.delete(my_contact)
        db.session.commit()
        # Log delete contact time
        time_deleted = time.ctime()
        with open("log.txt","a") as log:
            log.write(time_deleted)
            log.write("\n")
        flash('Deletado com sucesso.', 'danger')
    except:
        db.session.rollback()
        flash('Erro ao deletar contato.', 'danger')

    return redirect(url_for('contacts'))


if __name__ == "__main__":
    app.run(debug=True)
