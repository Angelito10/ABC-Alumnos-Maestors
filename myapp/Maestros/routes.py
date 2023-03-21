from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from Maestros import forms
from Maestros import main
from db import get_connection

maestros = Blueprint('maestros',__name__)

@maestros.route("/Maestros",methods = ['GET','POST'])
def index():
    create_from = forms.MaestroForm(request.form)
    if request.method == 'POST':
        matricula = create_from.matricula.data
        nombre = create_from.nombre.data
        apaterno = create_from.apaterno.data
        amaterno = create_from.amaterno.data
    
        main.agregar_maestros(nombre=nombre, apaterno=apaterno, amaterno=amaterno,matricula=matricula)
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('Maestros.html', form = create_from)

@maestros.route("/ABCompletoMaestros",methods = ['GET','POST'])
def ABCompleto():
    create_from = forms.MaestroForm(request.form)
    maestros = main.getAllMaestros()
    return render_template('ABCompletoMaestros.html',form = create_from, maestros = maestros)

@maestros.route('/modificarMaestros', methods = ['GET','POST'])
def modificar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')
    if request.method == 'GET':

        t = main.getAllMestroById(matricula)
        
        create_form.id.data = t[0]
        create_form.matricula.data = t[4]
        create_form.nombre.data = t[1]
        create_form.apaterno.data = t[2]
        create_form.amaterno.data = t[3]

        
    if request.method == 'POST':
        id = create_form.id.data
        nombre = create_form.nombre.data
        apaterno = create_form.apaterno.data
        amaterno = create_form.amaterno.data
        

        main.modificar_maestros(nombre=nombre,apaterno=apaterno,amaterno=amaterno,id=id)
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('modificarMaestros.html', form = create_form)

@maestros.route('/eliminarMaestros', methods = ['GET','POST'])
def eliminar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')
    if request.method == 'GET':
        t = main.getAllMestroById(matricula)
        
        create_form.id.data = t[0]
        create_form.matricula.data = t[4]
        create_form.nombre.data = t[1]
        create_form.apaterno.data = t[2]
        create_form.amaterno.data = t[3]
        
    if request.method == 'POST':
        id = create_form.id.data        
        main.eliminar_maestros(id=id)
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('eliminarMaestros.html', form = create_form)