from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from warehouse.models import Item, Instance
from warehouse.views import Items, DeleteViewCustom, Instances, MyStuff

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^items$', Items.as_view(), name='items'),
    url(r'^$', Items.as_view(), name='items'),
    url(r'^item/(?P<pk>\d+)/delete/$', DeleteViewCustom.as_view(model=Item, success_url=reverse_lazy("wh:items") ), name='item-delete'),
    url(r'^instances$', Instances.as_view(), name='instances'),
    url(r'^item/(?P<pk>\d+)/delete/$', DeleteViewCustom.as_view(model=Instance, success_url=reverse_lazy("wh:instances") ), name='instance-delete'),
    url(r'^instance/(?P<pk>\d+)/view$', DetailView.as_view(model = Instance, template_name='instance_detail.html'), name='instance-detail'),
    url(r'^mystuff$', MyStuff.as_view(), name='mystuff'),
)
