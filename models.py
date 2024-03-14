from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Empleado(db.Model):
  __tablename__ = 'empleados'
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50))
  direccion = db.Column(db.String(50))
  telefono = db.Column(db.String(20))
  email = db.Column(db.String(50))
  sueldo = db.Column(db.Float)
  create_date = db.Column(db.DateTime, default=datetime.datetime.now)
  
class Pizza(db.Model):
  __tablename__ = 'pizza'
  id=db.Column(db.Integer,primary_key=True)
  nombre = db.Column(db.String(50))
  direccion = db.Column(db.String(50))
  telefono = db.Column(db.String(20))
  tamanio=db.Column(db.String(50))
  ingredientes =db.Column(db.String(100))
  numeroPizzas =db.Column(db.Integer)
  subtotal =db.Column(db.String(50))
  fecha=db.Column(db.DateTime)
  dia=db.Column(db.String(50))
  create_date=db.Column(db.DateTime,default=datetime.datetime.now)
  
class Venta(db.Model):
  __tablename__ = 'venta'
  id=db.Column(db.Integer,primary_key=True)
  nombre = db.Column(db.String(50))  
  numeroPizzas =db.Column(db.Integer)
  total =db.Column(db.String(50))
  fecha=db.Column(db.DateTime)
  dia=db.Column(db.String(50))
  create_date=db.Column(db.DateTime,default=datetime.datetime.now)