from flask import Flask 
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from Alumnos.alumnos import db


app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')


from Alumnos.routes import alumnos as alumnos_blueprint
app.register_blueprint(alumnos_blueprint)

from Maestros.routes import maestros as maestros_blueprint
app.register_blueprint(maestros_blueprint)



if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)