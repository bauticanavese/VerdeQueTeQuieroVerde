from django import forms

class EventForm(forms.Form):
    name = forms.CharField(label = 'Nombre y apellido', max_length = 50)
    email = forms.EmailField(label = 'e-mail', max_length = 50)
