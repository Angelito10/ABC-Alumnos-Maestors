from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from Alumnos.alumnos import db
from Alumnos.alumnos import Alumnos
from Alumnos import forms


alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/Alumnos',methods = ['GET','POST'])
def index():
    create_from = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_from.nombre.data,
                       apellidos = create_from.apellidos.data,
                       email = create_from.email.data)
        
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('Alumnos.html',form = create_from)

@alumnos.route('/ABCompleto' , methods = ['GET','POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #SELECT * FROM alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos)

@alumnos.route("/modificar",methods = ['GET','POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #SELECT * FROM alumnos WHERE id == id
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        
    if request.method == 'POST':
        id = create_form.id.data
        #SELECT * FROM alumnos WHERE id == id
        alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumn.nombre = create_form.nombre.data
        alumn.apellidos = create_form.apellidos.data
        alumn.email = create_form.email.data
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('modificar.html', form = create_form)


@alumnos.route("/eliminar",methods = ['GET','POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #SELECT * FROM alumnos WHERE id == id
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        
    if request.method == 'POST':
        id = create_form.id.data
        #SELECT * FROM alumnos WHERE id == id
        alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        """ alumn.nombre = create_form.nombre.data
        alumn.apellidos = create_form.apellidos.data
        alumn.email = create_form.email.data """
        db.session.delete(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('eliminar.html', form = create_form)

