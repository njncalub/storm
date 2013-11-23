from django import forms
from stormapp.deadbodies.models import DeadBody

class DeadBodyForm(forms.ModelForm):
    class Meta:
        model = DeadBody
        exclude = {'date_reported', 'status', }