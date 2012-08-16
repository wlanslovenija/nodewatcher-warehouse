from django.http import HttpResponse
from forms import InstanceForm, ItemForm
from models import Item, Instance
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def list(request):
    return HttpResponse("Hello world!")

def view(request, id):
    return HttpResponse("Hello %s!" % id)

class Items(CreateView):
    form_class = ItemForm
    model = Item
    template_name = 'items.html'
    success_url = reverse_lazy('wh:items')
    
    def form_valid(self, form):
        import datetime
        form.instance.date_added = datetime.datetime.now().date()
        form.instance.last_change = datetime.datetime.now().date()
        return super(ItemAdd, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        from warehouse.models import Item
        
        context['item_list'] = Item.objects.all()
        return context

class DeleteViewCustom(DeleteView):
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class Instances(CreateView):
    form_class = InstanceForm
    model = Instance
    template_name = 'instances.html'
    success_url = reverse_lazy('wh:instances')

    def form_valid(self, form):
        import datetime
        form.instance.date_added = datetime.datetime.now().date()
        form.instance.last_change = datetime.datetime.now().date()
        return super(ItemAdd, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        from warehouse.models import Instance

        context['instance_list'] = Instance.objects.all()
        return context

