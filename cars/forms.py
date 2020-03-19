from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    model = forms.CharField(required=False)

    model.widget.attrs.update({'class': 'form-control' })

    class Meta:
        model = Car
        fields = ['manufacturer', 'model', 'year_of_issue', 'transmission', 'colour']
        widgets = {
            'manufacturer': forms.TextInput(attrs={'class':'form-control'}),
            # 'model': forms.TextInput(required=False, attrs={'class':'form-control'}),
            'year_of_issue': forms.NumberInput(attrs={'class':'form-control'}),
            'transmission': forms.Select(attrs={'class':'form-control'}),
            'colour': forms.TextInput(attrs={'class':'form-control'}),
        }