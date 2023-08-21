from django import forms
from .models import Logger
# from django.forms.widgets import NumberInput
# class DemoForm(forms.Form):
#     new_name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
# class DemoForm(forms.Form):
#     email = forms.EmailField(label='Enter email address')
# class DemoForm(forms.Form):
#     reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
FAVORITE_COCKTAIL = [
    ('longdrink', 'Longdrink'),
    ('shot', 'Shot'),
    ('sour', 'Sour'),
    ('non-alcoholic', 'Non-alcoholic'),
]

class DemoForm(forms.Form):
    # favorite_cocktail = forms.ChoiceField(choices=FAVORITE_COCKTAIL)
    favorite_cocktail = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COCKTAIL)

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
