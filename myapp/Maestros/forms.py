from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import EmailField
from wtforms import validators

class MaestroForm(Form):
    id = IntegerField('id')
    matricula = StringField('Matricula',[validators.DataRequired(message='Campo requerido')])
    nombre = StringField('Nombre', [validators.DataRequired(message='Campo requerido')])
    apaterno = StringField('Apellido Paterno', [validators.DataRequired(message='Campo requerido')])
    amaterno = StringField('Apellido Materno')
    