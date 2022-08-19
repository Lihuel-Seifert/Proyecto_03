from  django.forms import Form, CharField

class Busqueda(Form):
    buscar = CharField(max_length=150)
    
