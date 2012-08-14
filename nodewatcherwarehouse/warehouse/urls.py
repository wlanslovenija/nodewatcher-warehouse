from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from warehouse.models import Item, Instance
from warehouse.views import ItemAdd

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model = Item, template_name='item_list.html'), name='item-list'),
    url(r'^item/add$', ItemAdd.as_view(), name='item-add'),
    url(r'^instance/list$', ListView.as_view(model = Instance, template_name='instance_list.html'), name='instance-list'),
    url(r'^instance/view/(?P<pk>\d+)$', DetailView.as_view(model = Instance, template_name='instance_detail.html'), name='instance-detail'),
    url(r'^items/list$', ListView.as_view(model = Item, template_name='item_list.html'), name='item-list'),
    url(r'^view/(\d+)$', 'warehouse.views.view'),
    url(r'^admin/', include(admin.site.urls)),
)
