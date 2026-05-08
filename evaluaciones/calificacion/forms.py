from django import forms

from .models import Calificacion

class CalificacionForm(forms.ModelForm):

    class Meta:

        model = Calificacion

        fields = '__all__'

    def clean_nota(self):

        nota = self.cleaned_data['nota']

        if nota < 0 or nota > 10:

            raise forms.ValidationError(
                "La nota debe estar entre 0 y 10"
            )

        return nota