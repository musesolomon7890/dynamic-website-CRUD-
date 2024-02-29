from django import forms
from .models import Phone, RepairService

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'issue', 'repair_cost']

class RepairServiceForm(forms.ModelForm):
    class Meta:
        model = RepairService
        fields = ['name', 'description']
