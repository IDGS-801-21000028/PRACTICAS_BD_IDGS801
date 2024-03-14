from wtforms import Form
from wtforms import *
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

class MultiCheckboxField(SelectMultipleField):
  widget = widgets.ListWidget(prefix_label=False)
  option_widget = widgets.CheckboxInput()
  
class PizzeriaForms(Form):
  id = IntegerField('id',[
    validators.number_range(min=0, max=20, message="Valor no válido.")
  ])
  nombre = StringField('Nombre',[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  direccion = StringField("Dirección",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  telefono = TelField("Teléfono",[
    validators.DataRequired(message="El campo es requerido."),
    validators.length(min=4, max=15, message="Error en la longitud.")
  ])
  fechaCompra = DateField("Fecha Compra",[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  tamanio = RadioField("Tamaño Pizza", choices=[(40,"Chica $40"),(80, "Mediana $80"),(120, "Grande $120")], render_kw={'class':'form-check-input'}, validate_choice=False, validators=[
    validators.DataRequired(message="El campo es requerido."),
  ])
  ingr = MultiCheckboxField("Ingredientes", choices=[("Jamón","Jamón $10"),("Piña","Piña $10"),("Champiñones", "Champiñones $10")], validators=[
    validators.DataRequired(message="El campo es requerido. Selecciona un ingrediente."),
  ], render_kw={'class':'form-check-input'})
  numPizzas = IntegerField("Número de Pizzas",[
    validators.DataRequired(message="El campo es requerido."),
    validators.number_range(min=1, max=100, message="Valor no válido.")
  ])
  opTotales = RadioField("Ver por", choices=[(1,"Dia"),(2,"Mes")], render_kw={'class':'btn-check'}, validate_choice=False, validators=[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  opDia = BooleanField("Hoy", render_kw={"checked":"checked"})
  fechaConsulta = DateField("Fecha a Consultar",[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  mes = SelectField("Mes", choices=[('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'), ('4', 'Abril'),('5', 'Mayo'), ('6', 'Junio'), ('7', 'Julio'), ('8', 'Agosto'),('9', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], validators=[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  dia = SelectField("Día", choices=[('monday', 'Lunes'),('tuesday', 'Martes'),('wednesday', 'Miércoles'),('thursday', 'Jueves'),('friday', 'Viernes'),('saturday', 'Sábado'),('sunday', 'Domingo')],validators=[
    validators.DataRequired(message="El campo es requerido.")    
  ])
  
  agregar = SubmitField("Agregar")
  quitar = SubmitField("Quitar")
  modificar = SubmitField("Modificar")
  terminar = SubmitField("Terminar", render_kw={'data-toggle':"modal", 'data-target':"#exampleModal"})
  verDatos = SubmitField("Ver Totales")  
  enviarVenta = SubmitField("Confirmar")