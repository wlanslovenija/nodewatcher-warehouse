from django import template
register = template.Library()
from django.core.urlresolvers import reverse

def qr_code(obj, size=2):
    return reverse("wh:qr", kwargs={"string": abs_view(obj), "size":size})

def abs_view(obj):
    from django.contrib.sites.models import Site
    # TODO Somehow check for https?
    return "%s://%s%s" % ("http", Site.objects.get_current().domain, reverse("wh:item-detail", kwargs = {"pk" : obj.id}))

register.filter("qr_code", qr_code)
register.filter("abs_view", abs_view)