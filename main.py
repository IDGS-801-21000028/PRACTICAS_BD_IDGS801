import datetime
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import extract
from forms import *
from flask import flash
from flask_wtf.csrf import CSRFProtect
# from flask import g
from config import DevelopmentConfig

from models import db
from models import *

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

@app.route("/eliminar", methods = ['GET','POST'])
def eliminar():
  form_emp = EmpleadoForms(request.form)
  if request.method == 'GET':
    id = request.args.get('id')
    emp = db.session.query(Empleado).filter(Empleado.id==id).first()    
    form_emp.id.data = request.args.get('id')    
    form_emp.nombre.data = emp.nombre
    form_emp.direccion.data = emp.direccion
    form_emp.telefono.data = emp.telefono
    form_emp.email.data = emp.email
    form_emp.sueldo.data = emp.sueldo
  if request.method == 'POST':
    id = form_emp.id.data    
    alumno = Empleado.query.get(id)
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('ABC_Completo'))    
  return render_template("Eliminar.html", form=form_emp)

@app.route("/modificar", methods = ['GET','POST'])
def modificar():
  form_emp = EmpleadoForms(request.form)
  if request.method == 'GET':
    id = request.args.get('id')
    emp = db.session.query(Empleado).filter(Empleado.id==id).first()
    form_emp.id.data = request.args.get('id')    
    form_emp.nombre.data = emp.nombre
    form_emp.direccion.data = emp.direccion
    form_emp.telefono.data = emp.telefono
    form_emp.email.data = emp.email
    form_emp.sueldo.data = emp.sueldo
  if request.method == 'POST':
    id = form_emp.id.data    
    empleado = Empleado.query.get(id)
    empleado.nombre = form_emp.nombre.data,
    empleado.direccion = form_emp.direccion.data,
    empleado.telefono = form_emp.telefono.data,
    empleado.email = form_emp.email.data,
    empleado.sueldo = form_emp.sueldo.data
    db.session.add(empleado)
    db.session.commit()
    return redirect(url_for('ABC_Completo'))    
  return render_template("Modificar.html", form=form_emp)

@app.route("/ABC_Completo", methods = ['GET','POST'])
def ABC_Completo():
  empleados = Empleado.query.all()
  return render_template("ABC_Completo.html", empleados=empleados)

orden_list = []
ventas = []
@app.route("/pizzeria", methods = ['GET','POST'])
def Pizzeria():
  pzz = PizzeriaForms(request.form)  
  global orden_list, ventas
  pzz.id.validators = []
  mensaje = ""
  ventasTotales = 0.0
  modify = False
  # modi_act = False
  # map_tamanios = {
  #   "Chica": "40",
  #   "Mediana": "80",
  #   "Grande": "120"
  # }    
  if request.method == 'GET':
    pzz.fechaCompra.data = datetime.datetime.now().date()
    pzz.fechaConsulta.data = datetime.datetime.now().date()
  elif request.method == 'POST':
    pzz.fechaConsulta.data = datetime.datetime.now().date()
    pzz.fechaConsulta.validators = []
    pzz.opTotales.validators = []
    pzz.mes.validators = []
    pzz.dia.validators = []
    if "agregar" in request.form and pzz.validate():
      total = 0.0
      tamanio = ""      
      for v, texto, seleccionado, d in pzz.tamanio.iter_choices():
        if seleccionado:
          tamanio = texto.split("$")[0].strip()
      ingr_list = request.form.getlist('ingr')
      ingredientes = ', '.join(ingr_list)
      if len(ingr_list) >= 1:
        total = float((len(ingr_list) * 10) * int(pzz.numPizzas.data)) + (float(pzz.tamanio.data) * int(pzz.numPizzas.data))
      pizza = Pizza(
        nombre = pzz.nombre.data,
        direccion = pzz.direccion.data,
        telefono = pzz.telefono.data,
        tamanio = tamanio,
        ingredientes = ingredientes,
        numeroPizzas = pzz.numPizzas.data,
        subtotal = total,
        fecha = pzz.fechaCompra.data,
        dia = pzz.fechaCompra.data.strftime("%A").lower()
      )
      orden_list.append(pizza)
    if "quitar" in request.form:
      ordenes_seleccionadas = request.form.getlist('ordenes_seleccionadas')
      orden_list[:] = [orden for i, orden in enumerate(orden_list) if str(i) not in ordenes_seleccionadas]
    if "terminar" in request.form:
      if len(orden_list) == 0:
        mensaje = "Selecciona un producto"
        flash(mensaje)
      else:       
        totalVenta = sum(orden.subtotal for orden in orden_list)
        mensaje = "¿Desea confirmar la venta? El total es: {}".format(totalVenta)        
        flash(mensaje)
    if "enviarVenta" in request.form:   
      ord = orden_list[0]  
      venta = Venta(
        nombre = ord.nombre,
        numeroPizzas = sum(orden.numeroPizzas for orden in orden_list),
        total= sum(orden.subtotal for orden in orden_list),
        fecha = ord.fecha,
        dia = ord.dia
      )
      db.session.add(venta)
      db.session.commit()
      orden_list.clear()
      pzz = PizzeriaForms()
      pzz.fechaConsulta.data = datetime.datetime.now().date()        
    if "verDatos" in request.form:
      if pzz.opDia.data:
        if pzz.fechaConsulta.data == None:
          pzz.nombre.validators = []
          pzz.direccion.validators = []
          pzz.telefono.validators = []
          pzz.fechaCompra.validators = []
          pzz.tamanio.validators = []
          pzz.ingr.validators = []
          pzz.numPizzas.validators = []
          pzz.opTotales.validators = []
          pzz.mes.validators = []
          pzz.dia.validators = []
          pzz.validate()
        else:
          ventas = Venta.query.filter(Venta.fecha == pzz.fechaConsulta.data).all()
          ventasTotales = sum(int(v.total) for v in ventas)
      else :
        if pzz.mes.data == None or pzz.dia.data == None:
          pzz.nombre.validators = []
          pzz.direccion.validators = []
          pzz.telefono.validators = []
          pzz.fechaCompra.validators = []
          pzz.tamanio.validators = []
          pzz.ingr.validators = []
          pzz.numPizzas.validators = []
          pzz.opTotales.validators = []
          pzz.fechaConsulta.validators = []
          pzz.validate()
        else:               
          if pzz.opTotales.data == '1':
            ventas.clear()
            ventas = Venta.query.filter(Venta.dia == pzz.dia.data).all()
            ventasTotales = sum(int(v.total) for v in ventas)
          elif pzz.opTotales.data == '2':
            ventas.clear()
            ventas = Venta.query.filter(extract('month', Venta.fecha) == pzz.mes.data).all()
            ventasTotales = sum(int(v.total) for v in ventas)
    # if "modificar" in request.form:
    #   modify = True
    #   ordenes_seleccionadas = request.form.getlist('ordenes_seleccionadas')
    #   orden_seleccionada = next((orden for i, orden in enumerate(orden_list) if str(i) in ordenes_seleccionadas), None)
    #   if orden_seleccionada is not None:
     
    #     pzz.nombre.data = orden_seleccionada.nombre
    #     pzz.direccion.data = orden_seleccionada.direccion
    #     pzz.telefono.data = orden_seleccionada.telefono        
    #     pzz.tamanio.data = map_tamanios[orden_seleccionada.tamanio]
    #     pzz.ingr.data =  orden_seleccionada.ingredientes.split(', ') if orden_seleccionada.ingredientes else []
    #     print(pzz.fechaCompra.data, orden_seleccionada.fecha)
    #     pzz.fechaCompra.data = datetime.datetime.now().date()
    #     print(pzz.fechaCompra.data)
    #     pzz.numPizzas.data = orden_seleccionada.numeroPizzas                   
        
        # if pzz.validate():     
        #   tamanio = ""
        #   for v, texto, seleccionado, d in pzz.tamanio.iter_choices():
        #     if seleccionado:
        #       tamanio = texto.split("$")[0].strip()           
        #   orden_seleccionada.nombre = pzz.nombre.data
        #   orden_seleccionada.direccion = pzz.direccion.data
        #   orden_seleccionada.telefono = pzz.telefono.data
        #   orden_seleccionada.fecha = pzz.fechaCompra.data
        #   orden_seleccionada.tamanio = tamanio
        #   ingr_list = request.form.getlist('ingr')
        #   print(ingr_list)
        #   orden_seleccionada.ingredientes = ', '.join(ingr_list)
        #   orden_seleccionada.numeroPizzas = pzz.numPizzas.data            
        
  return render_template("pizzeria.html", form=pzz, ordenes=orden_list, ventas=ventas, totales=ventasTotales, modify=modify)

if __name__ == "__main__":  
  csrf.init_app(app)  
  db.init_app(app)
  
  with app.app_context():
    db.create_all()
        
  app.run()