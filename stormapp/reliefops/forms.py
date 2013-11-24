from django import forms
from stormapp.reliefops.models import ReliefOps

class RelOpsForm(forms.ModelForm):
    class Meta:
        model = ReliefOps