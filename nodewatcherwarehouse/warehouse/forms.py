from models import Item, Instance
from django import forms

from nodewatcher.nodes.models import Node

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('date_added', 'status_change', 'last_change')
        widgets = {
            'note': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }

class InstanceForm(forms.ModelForm):
    
    
    def label_member(self, obj):
        if obj.first_name:
            return "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)
        else:
            return obj.username
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields["node"].label_from_instance = lambda y: y.name
        self.fields["node"].queryset = Node.objects.regpoint("config").registry_fields(name = "GeneralConfig.name")
        
        self.fields["member"].label_from_instance = self.label_member
        
    
    class Meta:
        model = Instance
        exclude = ('date_added', 'status_change', 'last_change')
        widgets = {
            'note': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }
