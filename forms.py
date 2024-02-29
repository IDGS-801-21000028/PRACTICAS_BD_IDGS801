from wtforms import Form
from wtforms import StringField, IntegerField, TelField, FloatField
from wtforms import EmailField
from wtforms import validators
  
class EmpleadoForms(Form):
  id = IntegerField('id', [
    validators.number_range(min=0, max=20, message="Valor no válido.")
  ])
  nombre = StringField("Nombre",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])  
  direccion = StringField("Direccion",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  telefono = TelField("Teléfono",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=10, max=15, message="Error en la longitud.")
  ])
  email = EmailField("email", [
    validators.DataRequired(message="El campo es requerido."),
    validators.Email(message="Ingrese un correo valido")
  ])
  sueldo = FloatField("Sueldo", [
    validators.DataRequired(message="El campo es requerido.")
  ])