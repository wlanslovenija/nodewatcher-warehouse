from django.contrib.auth.decorators import login_required, user_passes_test

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from warehouse.models import *
from warehouse.views import *

from django.contrib import admin
admin.autodiscover()

def staff_required(view):
    return user_passes_test(lambda a: a.is_staff)(view)

urlpatterns = patterns('',
    url(r'^itemtype$', staff_required(ItemTypeView.as_view()), name='itemtype'),
    url(r'^itemtype/(?P<pk>\d+)/delete/$', staff_required(DeleteViewCustom.as_view(model=ItemType, success_url=reverse_lazy("wh:itemtype"))), name='itemtype-delete'),
    
    url(r'^item$', staff_required(ItemView.as_view()), name='item'),
    url(r'^item/(?P<pk>\d+)/delete/$', staff_required(DeleteViewCustom.as_view(model=Item, success_url=reverse_lazy("wh:item"))), name='item-delete'),
    url(r'^item/(?P<pk>\d+)/edit/$', staff_required(ItemUpdateView.as_view()), name='item-edit'),
    url(r'^item/(?P<pk>\d+)/view$', staff_required(ItemViewDetail.as_view()), name='item-detail'),
    url(r'^item/(?P<items>.*)/printlabel$', staff_required(print_label), name='item-printlabel'),
    
    url(r'^mystuff$', login_required(MyStuff.as_view()), name='mystuff'),
    url(r'^$', login_required(MyStuff.as_view()), name='mystuff'),
    
    url(r'^qr_api/(?P<size>\d{1,2})/(?P<string>.*)$', login_required(generate_qr), name='qr'),
)
