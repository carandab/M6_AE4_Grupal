from django import forms
import datetime

class EventoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha = forms.DateField()
    ubicacion = forms.CharField( )
    """ if fecha <= datetime.now():
        print("ERROR:No se puede crear un evento en el pasado")
 """
class ParticipanteForm(forms.Form):
    nombre = forms.CharField(max_length=100 )
    correo = forms.EmailField()