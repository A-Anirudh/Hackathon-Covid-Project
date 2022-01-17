from django import forms
from django.conf import settings

VACCINE_CHOICES = (
    ('Covaxin', 'Covaxin'),
    ('Covishield', 'Covishield'),
)

class VaccineCheckForm(forms.Form):
    vaccine_name = forms.ChoiceField(choices=VACCINE_CHOICES, required=True)
    pin = forms.IntegerField(required=True, max_value=999999, min_value=0)
    # date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=settings.DATE_INPUT_FORMATS)



class VerifyForm(forms.Form):
    mobile = forms.IntegerField(required=True)
