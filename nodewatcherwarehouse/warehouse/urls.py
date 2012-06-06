from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from nodewatcherwarehouse.warehouse.models import Item

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wlan_warehouse.views.home', name='home'),
    url(r'^items/list$', ListView.as_view(model = Item)),
    url(r'^view/(\d+)$', 'nodewatcherwarehouse.warehouse.views.view'),
)
