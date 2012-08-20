from django.http import HttpResponse
from forms import *
from models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, View, DetailView
from django.core.urlresolvers import reverse_lazy

class MyStuff(TemplateView):
    template_name = "mystuff.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        context["current_user"] = self.request.user
        context["member_items"] = self.request.user.warehouse_member_items.all()
        #context["member_nodes"] = self.request.user.warehouse_member_items.all()        
        # get current user
        # get his stuff from the warehouse
        # get stuff assogned to his nodes
        return context

class ItemViewDetail(DetailView):
    model = Item
    template_name='item_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context

class ItemTypeView(CreateView):
    form_class = ItemTypeForm
    model = ItemType
    template_name = 'itemtypes.html'
    success_url = reverse_lazy('wh:itemtype')
    
    def form_valid(self, form):
        import datetime
        form.instance.date_added = datetime.datetime.now().date()
        form.instance.last_change = datetime.datetime.now().date()
        return super(ItemTypeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        from warehouse.models import ItemType
        
        context['itemtype_list'] = ItemType.objects.all()
        return context

class DeleteViewCustom(DeleteView):
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class ItemView(CreateView):
    form_class = ItemForm
    model = Item
    template_name = 'items.html'
    success_url = reverse_lazy('wh:item')

    def form_valid(self, form):
        import datetime
        form.instance.date_added = datetime.datetime.now().date()
        form.instance.last_changed = datetime.datetime.now().date()
        form.instance.status_changed = datetime.datetime.now().date()
        return super(ItemView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        from warehouse.models import Item
        context['item_list'] = Item.objects.all()
        return context

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_form.html'
    form_class = ItemForm

def print_label(request, items):
    i = eval(items)
    # TODO printing
    # 63.5 x 38.1
    from PIL import Image
    
    response = HttpResponse(mimetype="image/png")
    #img.save(response, "PNG")
    return response

def generate_qr(request, string="", size=5, pix_size=4, return_image=False):
    import qrcode
    qr = qrcode.QRCode(
        version=size,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=pix_size,
        border=2,
    )
    qr.add_data(string)
    qr.make()
    img = qr.make_image()
    if return_image:
        return img
    response = HttpResponse(mimetype="image/png")
    img.save(response, "PNG")
    return response
