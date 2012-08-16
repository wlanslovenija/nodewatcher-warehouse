from django import template
register = template.Library()
from django.core.urlresolvers import reverse

def qr_code(obj, size=2):
    return reverse("wh:qr", kwargs={"string": reverse("wh:item-detail", kwargs = {"pk" : obj.id}), "size":size})

register.filter("qr_code", qr_code)