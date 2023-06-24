from django import forms
from .models import Equation


class Equation_form(forms.ModelForm):
    class Meta:
        model = Equation
        fields = ["Equation X", "Equation Y"]
        labels = {
            "Equation X": "equation_x",
            "Equation Y": "equation_y"
        }
        widgets = {
            "equation_x": forms.TextInput(attrs= {"class":"form-input"}),
            "equation_y": forms.TextInput(attrs={"class": "form-input"})
        }
