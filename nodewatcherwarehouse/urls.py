from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wlan_warehouse.views.home', name='home'),
    url(r'^warehouse/admin/', include(admin.site.urls)),
    url(r'^warehouse/', include('nodewatcherwarehouse.warehouse.urls', namespace='wh', app_name='wh')),
)
