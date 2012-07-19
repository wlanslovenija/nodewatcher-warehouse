from django.http import HttpResponse
from forms import InstanceForm, ItemForm
from models import Item, Instance
from django.views.generic.edit import CreateView

def list(request):
    return HttpResponse("Hello world!")

def view(request, id):
    return HttpResponse("Hello %s!" % id)

class ItemAdd(CreateView):
    form_class = ItemForm
    model = Item
    template_name = 'item_add.html'
    
    def form_valid(self, form):
        import datetime
        form.instance.date_added = datetime.datetime.now().date
        form.instance.status_change = datetime.datetime.now().date
        form.instance.last_change = datetime.datetime.now().date
        
        return super(ItemAdd, self).form_valid(form)