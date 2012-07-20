from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from nodewatcherwarehouse.warehouse.models import Item, Instance
from views import ItemAdd

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model = Item, template_name='item_list.html'), name='item-list'),
    url(r'^item/add$', ItemAdd.as_view(), name='item-add'),
    url(r'^instance/list$', ListView.as_view(model = Instance, template_name='instance_list.html'), name='instance-list'),
    url(r'^instance/view/(?P<pk>\d+)$', DetailView.as_view(model = Instance, template_name='instance_detail.html'), name='instance-detail'),
    url(r'^items/list$', ListView.as_view(model = Item, template_name='item_list.html'), name='item-list'),
    url(r'^view/(\d+)$', 'nodewatcherwarehouse.warehouse.views.view'),
)
