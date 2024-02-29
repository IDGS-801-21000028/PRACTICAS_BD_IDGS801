from flask import Flask, render_template, request
from forms import *
##from flask import flash
from flask_wtf.csrf import CSRFProtect
##from flask import g
from config import DevelopmentConfig

from models import db
from models import Empleado

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

@app.before_request
def before_request():
  ##g.nombre = "Diego"
  pass

@app.after_request
def after_reques(response):
  return response

@app.route("/", methods = ['GET','POST'])
def index():
  form_emp = EmpleadoForms(request.form)
  form_emp.id.validators = []
  if request.method == 'POST' and form_emp.validate():
    
    empleado = Empleado (
      nombre = form_emp.nombre.data,
      direccion = form_emp.direccion.data,
      telefono = form_emp.telefono.data,
      email = form_emp.email.data,
      sueldo = form_emp.sueldo.data
    )
    
    db.session.add(empleado)
    db.session.commit()  
    form_emp = EmpleadoForms()
    
  return render_template("index.html", form=form_emp)

@app.route("/ABC_Completo", methods = ['GET','POST'])
def ABCompleto():
  empleados = Empleado.query.all()
  print(empleados)

  return render_template("ABC_Completo.html", empleados=empleados)

if __name__ == "__main__":  
  csrf.init_app(app)  
  db.init_app(app)
  
  with app.app_context():
    db.create_all()
        
  app.run()