from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from warehouse.models import *
from warehouse.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^itemtype$', ItemTypeView.as_view(), name='itemtype'),
    url(r'^itemtype/(?P<pk>\d+)/delete/$', DeleteViewCustom.as_view(model=ItemType, success_url=reverse_lazy("wh:itemtype") ), name='itemtype-delete'),
    
    url(r'^item$', ItemView.as_view(), name='item'),
    url(r'^$', ItemView.as_view(), name='itemview'),
    url(r'^item/(?P<pk>\d+)/delete/$', DeleteViewCustom.as_view(model=Item, success_url=reverse_lazy("wh:item") ), name='item-delete'),
    url(r'^item/(?P<pk>\d+)/edit/$', DeleteViewCustom.as_view(model=Item, success_url=reverse_lazy("wh:item") ), name='item-edit'),
    url(r'^item/(?P<pk>\d+)/view$', DetailView.as_view(model = Item, template_name='item_detail.html'), name='item-detail'),
    
    url(r'^mystuff$', MyStuff.as_view(), name='mystuff'),
    
    url(r'^qr_api/(?P<size>\d{1,2})/(?P<string>.*)$', generate_qr, name='qr'),
)
