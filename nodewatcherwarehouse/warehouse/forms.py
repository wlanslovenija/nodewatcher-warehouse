from models import Item, Instance
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('date_added', 'status_change', 'last_change')

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        exclude = ('date_added', 'status_change', 'last_change')
