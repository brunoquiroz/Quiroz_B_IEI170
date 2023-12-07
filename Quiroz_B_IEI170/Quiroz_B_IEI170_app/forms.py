from django import forms
from Quiroz_B_IEI170_app.models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
