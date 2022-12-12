from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class FormularioContacto(forms.Form):
    #Nombre y apellido | correo | telefono | empresa | proyecto

    nombre = forms.CharField(label='Nombre', required=True)

    email = forms.CharField(label="Email", required=True)

    telefono = forms.CharField(label='Telefono')

    reunion = forms.DateField(label='Fecha de reunión', widget=DateInput, required=True)

    proyecto = forms.CharField(label='Proyecto', widget=forms.Textarea(attrs={"rows":"2"}), max_length=500)

