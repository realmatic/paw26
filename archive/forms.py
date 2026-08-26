from django import forms

from .models import Record, Material, Tool

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['category', 'status', 'title',  'production_date', 'procedures', 'notes']

        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'}),
        }


